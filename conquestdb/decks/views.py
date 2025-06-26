from django.shortcuts import render
from django.http import JsonResponse
from conquestdb.cardscode import Initfunctions


card_array = Initfunctions.init_player_cards()
planet_array = Initfunctions.init_planet_cards()
apoka_errata_array = Initfunctions.init_apoka_errata_cards()
images_dict = {}
cards_dict = {}
apoka_errata_dict = {}
banned_cards = ["Bonesinger Choir", "Squiggoth Brute", "Corrupted Teleportarium", "Gun Drones", "Archon's Palace",
                "Land Speeder Vengeance", "Sowing Chaos", "Smasha Gun Battery", "The Prince's Might",
                "Purveyor of Hubris", "Doom", "Exterminatus", "Mind Shackle Scarab",
                "Crypt of Saint Camila", "Warp Storm"]
for key in range(len(card_array)):
    cards_dict[card_array[key].name] = card_array[key]
    images_dict[card_array[key].image_name] = card_array[key]
for key in range(len(apoka_errata_array)):
    apoka_errata_dict[apoka_errata_array[key].image_name] = apoka_errata_array[key]


def decks(request):
    return render(request, "decks/home_decks.html")


def my_decks(request):
    return render(request, "decks/mydecks.html")


def create_deck(request):
    return render(request, "decks/createdeck.html")


def deck_data(request, room_name):
    return render(request, "decks/deck_data.html", {"room_name": room_name})


def ajax_view(request):
    return JsonResponse({'message': 'Invalid request'})
