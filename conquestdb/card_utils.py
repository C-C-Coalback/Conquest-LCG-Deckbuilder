

def convert_name_to_img_src(card_name):
    card_name = card_name.replace("\"", "")
    card_name = card_name.replace(" ", "_")
    card_name = card_name.replace(":", "")
    card_name = card_name.replace("'idden_Base", "idden_Base")
    card_name = card_name + ".jpg"
    card_name = "/static/images/CardImages/" + card_name
    return card_name


def convert_name_to_hyperlink(card_name):
    card_name = card_name.replace("\"", "")
    card_name = card_name.replace(" ", "_")
    card_name = card_name.replace(":", "")
    card_name = card_name.replace("'idden_Base", "idden_Base")
    card_name = "/cards/" + card_name
    return card_name


def convert_name_to_create_deck_hyperlink(card_name):
    card_name = card_name.replace("\"", "")
    card_name = card_name.replace(" ", "_")
    card_name = "/decks/create_deck/preload_warlord/" + card_name
    return card_name
