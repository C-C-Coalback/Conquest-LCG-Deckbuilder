import os


replacements = [("Call the Storm", "Call The Storm"),
                ("Reveal the Blade", "Reveal The Blade")]


cwd = os.getcwd()
print(cwd)
target_directory = cwd + "/decks/deckstorage/"
for file in os.listdir(target_directory):
    creator = target_directory + file
    creator_file = creator + "/"
    for deck_name in os.listdir(creator_file):
        print(creator_file + deck_name)
        content_file = creator_file + deck_name + "/content"
        with open(content_file, "r") as f:
            content = f.read()
        for i in range(len(replacements)):
            content = content.replace(replacements[i][0], replacements[i][1])
            print(content)
        with open(content_file, "w") as f:
            f.write(content)
target_directory = cwd + "/decks/publisheddecks/"
for file in os.listdir(target_directory):
    creator = target_directory + file
    creator_file = creator + "/"
    for deck_name in os.listdir(creator_file):
        print(creator_file + deck_name)
        content_file = creator_file + deck_name + "/content"
        with open(content_file, "r") as f:
            content = f.read()
        for i in range(len(replacements)):
            content = content.replace(replacements[i][0], replacements[i][1])
            print(content)
        with open(content_file, "w") as f:
            f.write(content)
