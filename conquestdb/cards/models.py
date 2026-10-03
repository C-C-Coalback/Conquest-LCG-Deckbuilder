from django.db import models

class Card(models.Model):
    # A stable ID from the CSV (not the row number), used to match rows on re-import
    code = models.CharField(max_length=200, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    faction = models.CharField(max_length=50)
    loyalty = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)
    card_type = models.CharField(max_length=50)
    cost = models.SmallIntegerField(null=True, blank=True)
    command = models.SmallIntegerField(null=True, blank=True)
    attack = models.SmallIntegerField(null=True, blank=True)
    health = models.SmallIntegerField(null=True, blank=True)
    shields = models.SmallIntegerField(null=True, blank=True)
    cycle = models.CharField(max_length=200)
    war_pack = models.CharField(max_length=200)
    keywords = models.CharField(null=True, max_length=200)
    useful_quantities = models.PositiveSmallIntegerField(null=True, blank=True)
    sector = models.CharField(max_length=200, null=True)
    green = models.BooleanField(null=True, blank=True)
    blue = models.BooleanField(null=True, blank=True)
    red = models.BooleanField(null=True, blank=True)
    resources = models.SmallIntegerField(null=True, blank=True)
    cards = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class RulesClarification(models.Model):
    card = models.ForeignKey(
        "Card", on_delete=models.CASCADE, related_name="clarifications"
    )
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)
    source = models.CharField(max_length=200, blank=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]
        constraints = [
            models.UniqueConstraint(fields=["card", "order"], name="uniq_clarification_card_order"),
        ]


class CardFAQ(models.Model):
    card = models.ForeignKey(
        "Card", on_delete=models.CASCADE, related_name="faqs"
    )
    related_cards = models.ManyToManyField(
        "Card", blank=True, related_name="mentioned_in_faqs"
    )
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]
        constraints = [
            models.UniqueConstraint(fields=["card", "order"], name="uniq_faq_card_order"),
        ]