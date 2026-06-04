import os


def get_deck_given_key(key_string):
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/"
    for username in os.listdir(target_directory):
        if username:
            second_target_directory = target_directory + "/" + username
            if os.path.exists(second_target_directory + "/" + key_string):
                with open(second_target_directory + "/" + key_string + "/content", "r", encoding="utf-8") as d:
                    return d.read()
    target_directory = directory + "/decks/publisheddecks/"
    for username in os.listdir(target_directory):
        if username:
            second_target_directory = target_directory + "/" + username
            if os.path.exists(second_target_directory + "/" + key_string):
                with open(second_target_directory + "/" + key_string + "/content", "r", encoding="utf-8") as d:
                    return d.read()
    return ""
