# Conquest-LCG-Deckbuilder

Repo for the Warhammer 40k Conquest deckbuilder website using Python Django.

# Why create a new repo instead of using the various public ones of github?

They are written in TypeScript; great idea if you want a website to run fast and handle heavy traffic, 
terrible idea for making something fast. I am focusing on development speed 
here, and it is faster to just rewrite the whole thing in Python Django.

# What is this?

Warhammer 40k Conquest card game. See the Board Game Geek page: https://boardgamegeek.com/boardgame/156776/warhammer-40000-conquest

Here is a link to The Hive Tyrant's tutorial for the game: https://www.youtube.com/watch?v=NE8NL9PfjXU

# What is the current progress?

Haven't done this in a while. Seriously, this is an impressive crop. Great vegetables.

All done; things I want to do though:

- More graphs/statistics on the adv. deck details page.
- Separate decks into pages.
- Add support to search + filter decks.
- Rework deck lookup logic to use a dataframe.
- Add support for viewing user profiles.

# How can I run it myself?

(This assumes you have a general idea about how to use python and git already.)

First run "py -m pip install -r requirements.txt" to install dependencies.

Then, you need to run "py manage.py makemigrations", followed by "py manage.py migrate" to create the user database.

Now run "py manage.py runserver", and it should work.