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

TBD; unsure what to aim for yet, so nothing is quite set in stone. We already have an AJAX cards lookup system and log-in system. The card data is also already initialised.

# How can I run it myself?

First run "py -m pip install -r requirements.txt" to install dependencies.

Then, you need to run "py manage.py makemigrations", followed by "py manage.py migrate" to create the user database.

Now run "py manage.py runserver", and it should work.