from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from cards.models import Card, CardFAQ, RulesClarification

def parse_entry(path):
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n").strip()
    head, sep, body = raw.partition("\n---\n")
    if not sep:
        return {}, raw
    headers = {}
    for line in head.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip().lower()] = value.strip()
    return headers, body.strip()


class Command(BaseCommand):
    help = "Import rules clarifications and FAQs from a directory tree"

    def add_arguments(self, parser):
        parser.add_argument("root", help="Path to the rules directory")
        parser.add_argument(
            "--prune",
            action="store_true",
            help="Delete entries whose file no longer exists",
        )

    def handle(self, *args, **opts):
        root = Path(opts["root"])
        if not root.is_dir():
            raise CommandError(f"{root} is not a directory")

        with transaction.atomic():
            self.import_clarifications(root / "clarifications", opts["prune"])
            self.import_faqs(root / "faq", opts["prune"])

    # ------------------------------------------------------------------ #

    def iter_entries(self, base):
        """Yield (card, order, path) for every numbered file under base/<card code>/."""
        if not base.is_dir():
            return
        for card_dir in sorted(p for p in base.iterdir() if p.is_dir()):
            try:
                card = Card.objects.get(code=card_dir.name)
            except Card.DoesNotExist:
                self.stderr.write(f"Skipping {card_dir}: no card with code '{card_dir.name}'")
                continue
            for path in sorted(card_dir.iterdir()):
                if path.is_file() and path.stem.isdigit():
                    yield card, int(path.stem), path

    def import_clarifications(self, base, prune):
        seen = {}  # card.pk -> set of orders
        count = 0
        for card, order, path in self.iter_entries(base):
            headers, body = parse_entry(path)
            RulesClarification.objects.update_or_create(
                card=card,
                order=order,
                defaults={"text": body, "source": headers.get("source", "")},
            )
            seen.setdefault(card.pk, set()).add(order)
            count += 1
        if prune:
            self.prune(RulesClarification, base, seen)
        self.stdout.write(f"Clarifications: {count} imported")

    def import_faqs(self, base, prune):
        seen = {}
        count = 0
        for card, order, path in self.iter_entries(base):
            headers, body = parse_entry(path)
            question = headers.get("question")
            if not question:
                raise CommandError(f"{path}: missing 'question:' header")

            faq, _ = CardFAQ.objects.update_or_create(
                card=card,
                order=order,
                defaults={"question": question, "answer": body},
            )

            codes = [c.strip() for c in headers.get("related", "").split(",") if c.strip()]
            related = Card.objects.filter(code__in=codes)
            missing = set(codes) - {c.code for c in related}
            if missing:
                self.stderr.write(f"{path}: unknown related card codes {sorted(missing)}")
            faq.related_cards.set(related)

            seen.setdefault(card.pk, set()).add(order)
            count += 1
        if prune:
            self.prune(CardFAQ, base, seen)
        self.stdout.write(f"FAQs: {count} imported")

    def prune(self, model, base, seen):
        """Delete entries for cards that have a directory but no longer have that file."""
        for card_dir in base.iterdir() if base.is_dir() else []:
            if not card_dir.is_dir():
                continue
            card = Card.objects.filter(code=card_dir.name).first()
            if card:
                model.objects.filter(card=card).exclude(order__in=seen.get(card.pk, set())).delete()