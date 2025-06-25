from django.shortcuts import render, redirect
from conquestdb.cardscode import Initfunctions
import pandas as pd
from django.http import JsonResponse


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

df = pd.DataFrame([x.as_dict() for x in card_array])


def index(request):
    return render(request, 'cards/index.html')


# View to handle the Ajax request
def ajax_view(request):
    if request.method == 'POST':
        card_names = []
        search = request.POST.get('search')
        if search in cards_dict:
            image_name = cards_dict[search].image_name
            return JsonResponse({'message': "REDIRECT", 'cards': card_names, 'image_names': [image_name]})
        faction = request.POST.get('faction')
        traits = request.POST.get('traits')
        card_type = request.POST.get('card_type')
        shields = request.POST.get('shields')
        min_cost = -1
        max_cost = -1
        min_command = -1
        max_command = -1
        min_attack = -1
        max_attack = -1
        min_health = -1
        max_health = -1
        try:
            print(request.POST.get('min-cost'))
            min_cost = int(request.POST.get('min-cost'))
        except:
            pass
        try:
            max_cost = int(request.POST.get('max-cost'))
        except:
            pass
        try:
            min_command = int(request.POST.get('min-command'))
        except:
            pass
        try:
            max_command = int(request.POST.get('max-command'))
        except:
            pass
        try:
            min_attack = int(request.POST.get('min-attack'))
        except:
            pass
        try:
            max_attack = int(request.POST.get('max-attack'))
        except:
            pass
        try:
            min_health = int(request.POST.get('min-health'))
        except:
            pass
        try:
            max_health = int(request.POST.get('max-health'))
        except:
            pass
        print(min_cost)
        loyalty = request.POST.get('loyalty')
        filtered_df = df
        if traits:
            filtered_df = filtered_df[filtered_df['traits'].str.contains(traits)]
        if search is not None:
            filtered_df = filtered_df[filtered_df['name'].str.contains(search)]
        if shields != "-1":
            shields = int(shields)
            print(shields)
            filtered_df = filtered_df.loc[filtered_df['shields'] == shields]
        if faction != "None":
            filtered_df = filtered_df.loc[filtered_df['faction'] == faction]
        if loyalty != "None":
            filtered_df = filtered_df.loc[filtered_df['loyalty'] == loyalty]
        if card_type != "None":
            filtered_df = filtered_df.loc[filtered_df['card type'] == card_type]
        if min_cost != -1:
            filtered_df = filtered_df.loc[filtered_df['cost'] >= min_cost]
        if max_cost != -1:
            filtered_df = filtered_df.loc[filtered_df['cost'] <= max_cost]
        if min_command != -1:
            filtered_df = filtered_df.loc[filtered_df['command'] >= min_command]
        if max_command != -1:
            filtered_df = filtered_df.loc[filtered_df['command'] <= max_command]
        if min_attack != -1:
            filtered_df = filtered_df.loc[filtered_df['attack'] >= min_attack]
        if max_attack != -1:
            filtered_df = filtered_df.loc[filtered_df['attack'] <= max_attack]
        if min_health != -1:
            filtered_df = filtered_df.loc[filtered_df['health'] >= min_health]
        if max_health != -1:
            filtered_df = filtered_df.loc[filtered_df['health'] <= max_health]
        card_names = filtered_df['name'].to_list()
        image_names = filtered_df['image name'].to_list()
        message = f'Faction, {faction}'
        return JsonResponse({'message': message, 'cards': card_names, 'image_names': image_names})
    return JsonResponse({'message': 'Invalid request'})


def card_data(request, card_name):
    if card_name not in images_dict:
        return render(request, 'cards/index.html')
    card = images_dict[card_name]
    original_card_name = card.name
    image_name = card.image_name
    print(original_card_name)
    text = card.text
    card_type = card.card_type
    cost = str(card.cost)
    command = -1
    attack = -1
    health = -1
    bloodied_attack = -1
    bloodied_health = -1
    bloodied_text = -1
    shields = str(card.shields)
    is_unit = "False"
    loyalty = card.loyalty
    faction = card.faction
    traits = card.traits
    if card.is_unit:
        if card_type != "Warlord":
            card_type = card_type + " Unit"
            command = str(card.command)
        else:
            bloodied_text = card.bloodied_text
            bloodied_attack = card.bloodied_attack
            bloodied_health = card.bloodied_health
        is_unit = "True"
        attack = str(card.attack)
        health = str(card.health)
    errata_text = "No Errata"
    ban_text = "No Bans"
    if card_name in apoka_errata_dict:
        errata_text = "There is Errata"
    if original_card_name in banned_cards:
        ban_text = "Banned"
    return render(request, "cards/card_data.html",
                  {"card_name": original_card_name, "image_name": image_name, "text": text,
                   "card_type": card_type, "cost": cost, "command": command, "attack": attack, "health": health,
                   "is_unit": is_unit, "loyalty": loyalty, "faction": faction, "traits": traits,
                   "ban_text": ban_text, "errata_text": errata_text, "shields": shields,
                   "bloodied_attack": bloodied_attack, "bloodied_health": bloodied_health,
                   "bloodied_text": bloodied_text})
