from django.shortcuts import render


def decks(request):
    return render(request, "decks/home_decks.html")


def deck_data(request, room_name):
    return render(request, "decks/deck_data.html", {"room_name": room_name})
