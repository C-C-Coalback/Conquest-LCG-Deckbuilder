from django.shortcuts import render
from django.http import JsonResponse
from conquestdb.cardscode import Initfunctions
from conquestdb.cardscode import FindCard


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


alignment_wheel = ["Astra Militarum", "Space Marines", "Tau", "Eldar", "Dark Eldar", "Chaos", "Orks"]


def decks(request):
    return render(request, "decks/home_decks.html")


def my_decks(request):
    return render(request, "decks/mydecks.html")


def create_deck(request):
    return render(request, "decks/createdeck.html")


def deck_data(request, room_name):
    return render(request, "decks/deck_data.html", {"room_name": room_name})


def ajax_view(request):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        if flag == "ADDCARD":
            card_name = request.POST.get('card_name')
            if card_name not in cards_dict:
                return JsonResponse({'message': 'Card not found in database'})
            card = FindCard.find_card(card_name, card_array, cards_dict)
            if card.get_card_type() == "Warlord":
                message = "Warlord"
                name_warlord = card.get_name()
                faction = card.get_faction()
                sig_squad = card.signature_squad
                return JsonResponse({'message': message, 'warlord': name_warlord,
                                     'sig_squad': sig_squad, 'main_faction': faction})
            elif card.get_loyalty() == "Signature":
                return JsonResponse({'message': 'Can not add Signature units'})
            card_type = card.get_card_type()
            warlord_name = request.POST.get('warlord_name')
            print(warlord_name)
            warlord = FindCard.find_card(warlord_name, card_array, cards_dict)
            main_faction = warlord.get_faction()
            ally = request.POST.get('ally_faction')
            ally_ok = False
            if main_faction == card.get_faction():
                ally_ok = True
            elif main_faction == "Necrons":
                if card.get_faction() == "Neutral" or (card.get_faction() != "Tyranids" and card_type == "Army"):
                    ally_ok = True
            elif main_faction == "Tyranids":
                if card.get_faction() == "Tyranids" or (card.get_faction() == "Neutral" and card_type != "Army"):
                    ally_ok = True
            elif warlord_name == "Commander Starblaze":
                if ally == "Astra Militarum" and card.get_faction() == "Astra Militarum" and\
                        card.get_loyalty() == "Common":
                    ally_ok = True
            elif warlord_name == "Gorzod":
                if (card.get_faction() == "Space Marines" or card.get_faction() == "Astra Militarum") and \
                        card_type == "Army" and card.get_loyalty() == "Common" and card.check_for_a_trait("Vehicle"):
                    ally_ok = True
            else:
                print('got here')
                position_main_faction = -1
                for i in range(len(alignment_wheel)):
                    if alignment_wheel[i] == ally:
                        position_main_faction = i
                if position_main_faction != -1:
                    ally_pos_1 = (position_main_faction + 1) % 7
                    ally_pos_2 = (position_main_faction - 1) % 7
                    if ally == alignment_wheel[ally_pos_1] or ally == alignment_wheel[ally_pos_2]:
                        ally_ok = True
                print('got here')
            if ally_ok:
                return JsonResponse({'message': 'ADDCARD', 'card_type': card_type,
                                     'card_name': card_name})
            else:
                return JsonResponse({'message': 'Card not added'})

    return JsonResponse({'message': 'Invalid request'})
