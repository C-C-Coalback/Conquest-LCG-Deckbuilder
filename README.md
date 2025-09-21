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
- ~~Separate decks into pages.~~
- Add support to search + filter decks.
- Rework deck lookup logic to use a dataframe.
- Add support for viewing user profiles.

# How can I run it myself?

Runs python 3.9.7. You will need to already have git and python installed on your machine.

```
git clone https://github.com/C-C-Coalback/Conquest-LCG-Deckbuilder conquestdbrepo
cd conquestdbrepo
pip install -r "requirements.txt"
cd conquestdb
py manage.py makemigrations
py manage.py migrate
```

The website is ready to launch. There are not tests to run (yet). To run the website, 

```
py manage.py runserver
```
and navigate to "http://127.0.0.1:8000/" in your browser

Replace "py"s with "python" or "python3" if needed.
You should really probably be installing the requirements in a virtual environment but that is not necessary so is left as an exercise to the reader.

# Additional credits

Venite Adoremus font by Chequered Ink. https://www.dafont.com/venite-adoremus.font