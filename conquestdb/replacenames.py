import os


cwd = os.getcwd()
print(cwd)
target_directory = cwd + "/decks/deckstorage/"
for file in os.listdir(target_directory):
    creator = target_directory + file
    creator_file = creator + "/"
    for deck_name in os.listdir(creator_file):
        print(creator_file + deck_name)
        key_file = creator_file + deck_name + "/key"
        with open(key_file, "r") as f:
            key = f.read()
        os.rename(creator_file + deck_name, creator_file + key)
target_directory = cwd + "/decks/publisheddecks/"
for file in os.listdir(target_directory):
    creator = target_directory + file
    creator_file = creator + "/"
    for deck_name in os.listdir(creator_file):
        print(creator_file + deck_name)
        key_file = creator_file + deck_name + "/key"
        with open(key_file, "r") as f:
            key = f.read()
        os.rename(creator_file + deck_name, creator_file + key)
