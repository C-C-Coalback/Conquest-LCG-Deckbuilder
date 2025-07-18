from django.shortcuts import render, redirect
from conquestdb.cardscode import Initfunctions
import pandas as pd
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import os
import os.path
import datetime


card_array = Initfunctions.init_player_cards()
planet_array = Initfunctions.init_planet_cards()
apoka_errata_array = Initfunctions.init_apoka_errata_cards()
images_dict = {}
cards_dict = {}
apoka_errata_dict = {}
banned_cards = ["Bonesinger Choir", "Squiggoth Brute", "Corrupted Teleportarium", "Gun Drones", "Archon's Palace",
                "Land Speeder Vengeance", "Sowing Chaos", "Smasha Gun Battery", "The Prince's Might",
                "Purveyor of Hubris", "Doom", "Exterminatus", "Mind Shackle Scarab",
                "Crypt of Saint Camila", "Warpstorm"]
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
        redirect_enabled = request.POST.get('redirect-enabled')
        if search in cards_dict and redirect_enabled == "Yes":
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
        loyalty = request.POST.get('loyalty')
        filtered_df = df
        if traits:
            filtered_df = filtered_df[filtered_df['traits'].str.contains(traits)]
        if search is not None:
            filtered_df = filtered_df[filtered_df['name'].str.contains(search)]
        if shields != "-1":
            shields = int(shields)
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
        loyalties = filtered_df['loyalty'].to_list()
        card_types = filtered_df['card type'].to_list()
        factions = filtered_df['faction'].to_list()
        image_names = filtered_df['image name'].to_list()
        message = f'Faction, {faction}'
        return JsonResponse({'message': message, 'cards': card_names, 'image_names': image_names,
                             'loyalties': loyalties, 'card_types': card_types, 'factions': factions})
    return JsonResponse({'message': 'Invalid request'})


def card_data(request, card_name):
    directory = os.getcwd()
    target_directory = directory + "/cards/comments/" + card_name + "/"
    if request.method == 'POST':
        flag = request.POST.get('flag')
        if flag == "POST":
            username = request.POST.get('username')
            if not username:
                username = "Anonymous"
            comment = request.POST.get('comment')
            time = str(datetime.datetime.now())
            os.makedirs(target_directory, exist_ok=True)
            file_id = len([name for name in os.listdir(target_directory) if os.path.isfile(target_directory + "/" + name)])
            name_file = str(file_id) + ".txt"
            with open(target_directory + name_file, 'w') as file:
                file.write(username + "\n" + time + "\n" + comment)
        elif flag == "DELETE":
            # username = request.POST.get('username')
            id_c = request.POST.get('idcomment')
            name_file = id_c + ".txt"
            with open(target_directory + name_file, 'w') as file:
                file.write("")
    if card_name not in images_dict:
        return render(request, 'cards/index.html')
    card = images_dict[card_name]
    original_card_name = card.name
    image_name = card.image_name
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
    names_comments = []
    times_comments = []
    comments = []
    comment_ids = []
    no_comments = True
    if os.path.exists(target_directory):
        for infile in sorted(os.listdir(target_directory)):
            with open(target_directory + infile, 'r') as file:
                t = file.read()
                split_text = t.split("\n")
                if len(split_text) >= 3:
                    split_text[2] = "\n".join(split_text[2:])
                    idf = infile.split(sep=".")[0]
                    comment_ids.append(idf)
                    names_comments.append(split_text[0])
                    times_comments.append(split_text[1])
                    comments.append(split_text[2])
                    no_comments = False
    my_comments = zip(names_comments, times_comments, comments, comment_ids)
    return render(request, "cards/card_data.html",
                  {"card_name": original_card_name, "image_name": image_name, "text": text,
                   "card_type": card_type, "cost": cost, "command": command, "attack": attack, "health": health,
                   "is_unit": is_unit, "loyalty": loyalty, "faction": faction, "traits": traits,
                   "ban_text": ban_text, "errata_text": errata_text, "shields": shields,
                   "bloodied_attack": bloodied_attack, "bloodied_health": bloodied_health,
                   "bloodied_text": bloodied_text, "comments": my_comments, "noc": no_comments})
