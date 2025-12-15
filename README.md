# Conquest-LCG-Deckbuilder

Repo for the Warhammer 40k Conquest deckbuilder website using Python Django.

# What is this?

Warhammer 40k Conquest card game deckbuilder. See the Board Game Geek page:
https://boardgamegeek.com/boardgame/156776/warhammer-40000-conquest

Here is a link to The Hive Tyrant's tutorial for the game:
https://www.youtube.com/watch?v=NE8NL9PfjXU

# What is the current progress?

Haven't done this in a while. Seriously, this is an impressive crop. 
Great vegetables.

Just left with converting the deck lookup logic to use a dataframe now, 
though I am honestly not too bothered by it; the website is already very
fast, so the extra speed from the dataframe probably isn't noticeable 
enough to bother with.

- ~~More graphs/statistics on the adv. deck details page.~~
- ~~Separate decks into pages.~~
- ~~Add support to search + filter decks.~~
- Rework deck lookup logic to use a dataframe.
- ~~Add support for viewing user profiles.~~

# How can I run it myself?

Runs python 3.9.7. You will need to already have git and python 
installed on your machine.

```
git clone https://github.com/C-C-Coalback/Conquest-LCG-Deckbuilder conquestdbrepo
cd conquestdbrepo
pip install -r "requirements.txt"
cd conquestdb
py manage.py makemigrations
py manage.py migrate
```

The website is ready to launch. There are not tests to run (yet). 
To run the website, 

```
py manage.py runserver
```
and navigate to "http://127.0.0.1:8000/" in your browser

Replace "py"s with "python" or "python3" if needed.
You should really probably be installing the requirements in a
virtual environment but that is not necessary so is left as an 
exercise to the reader.

# Other userful functionality

The website supports exporting decks to the
[Tabletop Simulator](https://steamcommunity.com/sharedfiles/filedetails/?id=2471847304) addon.
Copy your Deck Key, found on the page for the deck or in the 
search results, then paste it into the text field in the addon. 
Your deck will appear from the centre of the table.

Please note that it is possible, though very rare, for the addon to spawn 
two decks in the same place if both are imported at the same time. 
This does not impact gameplay much, but it is a bit annoying when it happens,
since you will need to split the decks. To avoid this, move your deck 
to your HQ/deck area before importing the second one, 
and this will not be able to occur.

Additional APIs can be added as requested.

# Adjusting the TTS addon to request decks from your local host

Download the TTS addon. In the scripting section, there will be a text entry area. Here, 
change the site url from "conquestdb.com/api/tts/" to
"127.0.0.1:8000/api/tts/". Save this addon. You will now be able to 
import decks from your locally hosted conquestdb into the addon.

# Additional credits

Faction icon SVGs stolen from [zzorba](https://github.com/zzorba), creator of the previous conquestdb site.

Many thanks to warder808 for allowing me to configure his TTS addon to 
support importing decks from the site.