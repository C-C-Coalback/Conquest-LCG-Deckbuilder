from django.shortcuts import render
from django.http import JsonResponse
from conquestdb.cardscode import Initfunctions
from conquestdb.cardscode import FindCard
from django.http import HttpResponseRedirect
import light_dark_dict
import pandas as pd
import os
import copy
import datetime
import random
import string
import shutil


card_array = Initfunctions.init_player_cards()
card_names_array = []
for i in range(len(card_array)):
    card_names_array.append(card_array[i].get_name())
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
pledges_array = []
for i in range(len(card_array)):
    if card_array[i].check_for_a_trait("Pledge"):
        pledges_array.append(card_array[i].get_name())
temp_cwd = os.getcwd()
target_dir_temp = temp_cwd + "/decks/publisheddecks/"
os.makedirs(target_dir_temp, exist_ok=True)

alignment_wheel = ["Astra Militarum", "Space Marines", "Tau", "Eldar", "Dark Eldar", "Chaos", "Orks"]


def check_if_key_in_use(key_string):
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/"
    for username in os.listdir(target_directory):
        if username:
            second_target_directory = target_directory + "/" + username
            for deck_name in os.listdir(second_target_directory):
                if os.path.exists(second_target_directory + "/" + deck_name + "/key"):
                    with open(second_target_directory + "/" + deck_name + "/key", "r") as f:
                        this_key = f.read()
                        if this_key == key_string:
                            return True
    target_directory = directory + "/decks/publisheddecks/"
    if os.path.exists(target_directory):
        for username in os.listdir(target_directory):
            if username:
                second_target_directory = target_directory + "/" + username
                for deck_name in os.listdir(second_target_directory):
                    if os.path.exists(second_target_directory + "/" + deck_name + "/key"):
                        with open(second_target_directory + "/" + deck_name + "/key", "r") as f:
                            this_key = f.read()
                            if this_key == key_string:
                                return True
    return False


def create_new_key():
    num_tries = 0
    set_key = False
    while not set_key:
        new_key = ''.join(random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits
        ) for _ in range(16 + num_tries))
        print(new_key)
        if not check_if_key_in_use(new_key):
            return new_key
        if num_tries > 100:
            return new_key
        num_tries += 1


def delete_private_deck(key_string, name_user):
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/"
    try:
        for username in os.listdir(target_directory):
            if username == name_user:
                second_target_directory = target_directory + "/" + username
                for deck_name in os.listdir(second_target_directory):
                    if os.path.exists(second_target_directory + "/" + deck_name + "/key"):
                        is_the_file = False
                        with open(second_target_directory + "/" + deck_name + "/key", "r") as f:
                            this_key = f.read()
                            if this_key == key_string:
                                is_the_file = True
                        if is_the_file:
                            shutil.rmtree(second_target_directory + "/" + deck_name)
                            return True
    except Exception as E:
        print(E)
    return False


def delete_published_deck(key_string, name_user):
    directory = os.getcwd()
    target_directory = directory + "/decks/publisheddecks/"
    try:
        for username in os.listdir(target_directory):
            if username == name_user:
                second_target_directory = target_directory + "/" + username
                for deck_name in os.listdir(second_target_directory):
                    if os.path.exists(second_target_directory + "/" + deck_name + "/key"):
                        is_the_file = False
                        with open(second_target_directory + "/" + deck_name + "/key", "r") as f:
                            this_key = f.read()
                            if this_key == key_string:
                                is_the_file = True
                        if is_the_file:
                            shutil.rmtree(second_target_directory + "/" + deck_name)
                            return True
    except Exception as E:
        print(E)
    return False


def convert_name_to_img_src(card_name):
    card_name = card_name.replace("\"", "")
    card_name = card_name.replace(" ", "_")
    card_name = card_name.replace("'idden_Base", "idden_Base")
    card_name = card_name + ".jpg"
    card_name = "/static/images/CardImages/" + card_name
    return card_name


def convert_name_to_hyperlink(card_name):
    card_name = card_name.replace("\"", "")
    card_name = card_name.replace(" ", "_")
    card_name = card_name.replace("'idden_Base", "idden_Base")
    card_name = "/cards/" + card_name
    return card_name


def convert_name_to_create_deck_hyperlink(card_name):
    card_name = card_name.replace("\"", "")
    card_name = card_name.replace(" ", "_")
    card_name = "/decks/create_deck/preload_warlord/" + card_name
    return card_name


astra_militarum_warlords = []
astra_militarum_img_srcs = []
astra_militarum_hyperlinks = []
space_marines_warlords = []
space_marines_img_srcs = []
space_marines_hyperlinks = []
tau_warlords = []
tau_img_srcs = []
tau_hyperlinks = []
eldar_warlords = []
eldar_img_srcs = []
eldar_hyperlinks = []
dark_eldar_warlords = []
dark_eldar_img_srcs = []
dark_eldar_hyperlinks = []
chaos_warlords = []
chaos_img_srcs = []
chaos_hyperlinks = []
orks_warlords = []
orks_img_srcs = []
orks_hyperlinks = []
tyranids_warlords = []
tyranids_img_srcs = []
tyranids_hyperlinks = []
necrons_warlords = []
necrons_img_srcs = []
necrons_hyperlinks = []
for i in range(len(card_array)):
    if card_array[i].get_card_type() == "Warlord":
        if card_array[i].get_faction() == "Astra Militarum":
            astra_militarum_warlords.append(card_array[i].get_name())
            astra_militarum_img_srcs.append(convert_name_to_img_src(card_array[i].get_name()))
            astra_militarum_hyperlinks.append(convert_name_to_create_deck_hyperlink(card_array[i].get_name()))
        if card_array[i].get_faction() == "Space Marines":
            space_marines_warlords.append(card_array[i].get_name())
            space_marines_img_srcs.append(convert_name_to_img_src(card_array[i].get_name()))
            space_marines_hyperlinks.append(convert_name_to_create_deck_hyperlink(card_array[i].get_name()))
        if card_array[i].get_faction() == "Tau":
            tau_warlords.append(card_array[i].get_name())
            tau_img_srcs.append(convert_name_to_img_src(card_array[i].get_name()))
            tau_hyperlinks.append(convert_name_to_create_deck_hyperlink(card_array[i].get_name()))
        if card_array[i].get_faction() == "Eldar":
            eldar_warlords.append(card_array[i].get_name())
            eldar_img_srcs.append(convert_name_to_img_src(card_array[i].get_name()))
            eldar_hyperlinks.append(convert_name_to_create_deck_hyperlink(card_array[i].get_name()))
        if card_array[i].get_faction() == "Dark Eldar":
            dark_eldar_warlords.append(card_array[i].get_name())
            dark_eldar_img_srcs.append(convert_name_to_img_src(card_array[i].get_name()))
            dark_eldar_hyperlinks.append(convert_name_to_create_deck_hyperlink(card_array[i].get_name()))
        if card_array[i].get_faction() == "Chaos":
            chaos_warlords.append(card_array[i].get_name())
            chaos_img_srcs.append(convert_name_to_img_src(card_array[i].get_name()))
            chaos_hyperlinks.append(convert_name_to_create_deck_hyperlink(card_array[i].get_name()))
        if card_array[i].get_faction() == "Orks":
            orks_warlords.append(card_array[i].get_name())
            orks_img_srcs.append(convert_name_to_img_src(card_array[i].get_name()))
            orks_hyperlinks.append(convert_name_to_create_deck_hyperlink(card_array[i].get_name()))
        if card_array[i].get_faction() == "Tyranids":
            tyranids_warlords.append(card_array[i].get_name())
            tyranids_img_srcs.append(convert_name_to_img_src(card_array[i].get_name()))
            tyranids_hyperlinks.append(convert_name_to_create_deck_hyperlink(card_array[i].get_name()))
        if card_array[i].get_faction() == "Necrons":
            necrons_warlords.append(card_array[i].get_name())
            necrons_img_srcs.append(convert_name_to_img_src(card_array[i].get_name()))
            necrons_hyperlinks.append(convert_name_to_create_deck_hyperlink(card_array[i].get_name()))


def clean_sent_deck(deck_message):
    print("Code to test if deck is ok")
    deck_sections = deck_message.split(sep="------------------"
                                           "----------------------------------------------------")
    print(deck_sections)
    individual_parts = []
    for i in range(len(deck_sections)):
        individual_parts += deck_sections[i].split(sep="\n")
    individual_parts = [x for x in individual_parts if x]
    return individual_parts


def second_part_deck_validation(deck):
    global card_array
    global cards_dict
    print("Size should be fine")
    name = deck[0]
    res = name != '' and all(c.isalnum() or c.isspace() for c in name)
    if len(name) > 27:
        return "Name too long"
    elif not res:
        return "Name contains non-alphanumeric characters"
    warlord_card = FindCard.find_card(deck[1], card_array, cards_dict)
    if warlord_card.get_card_type() != "Warlord":
        print("Card in Warlord position is not a warlord")
        return "Card in Warlord position is not a warlord"
    remaining_signature_squad = copy.deepcopy(warlord_card.get_signature_squad())
    print("Warlord name: ", warlord_card.get_name())
    print("Remaining signature squad list: ", remaining_signature_squad)
    factions = deck[2].split(sep=" (")
    if len(factions) == 2:
        factions[1] = factions[1][:-1]
    print(factions)
    warlord_matches = True
    if factions[0] != warlord_card.get_faction():
        print("Faction chosen does not match the warlord")
        return "Warlord does not match main faction"
    if len(factions) == 1 and warlord_matches:
        factions.append("None")
        return deck_validation(deck, remaining_signature_squad, factions, warlord_card.get_name())
    if len(factions) == 2 and warlord_matches:
        if factions[0] == factions[1]:
            print("Main faction and ally faction can not be the same")
            return "Main faction and ally faction can not be the same"
        position_main_faction = -1
        for faction in range(len(alignment_wheel)):
            if alignment_wheel[faction] == factions[0]:
                position_main_faction = faction
        if position_main_faction != -1:
            ally_pos_1 = (position_main_faction + 1) % 7
            ally_pos_2 = (position_main_faction - 1) % 7
            if warlord_card.get_name() == "Commander Starblaze":
                if factions[1] == "Astra Militarum":
                    return deck_validation(deck, remaining_signature_squad, factions, "Commander Starblaze")
            elif warlord_card.get_name() == "Farseer Tadheris":
                if factions[1] == "Space Marines" or factions[1] == "Orks":
                    return deck_validation(deck, remaining_signature_squad, factions, "Farseer Tadheris")
            elif factions[1] == alignment_wheel[ally_pos_1] \
                    or factions[1] == alignment_wheel[ally_pos_2]:
                return deck_validation(deck, remaining_signature_squad, factions)
        return "Issue with faction matching."
    return "Unknown issue"


def deck_validation(deck, remaining_signature_squad, factions, warlord=""):
    global card_array
    global cards_dict
    print("Can continue")
    current_index = 4
    holy_crusade_relevant = False
    if deck[current_index] == "Signature Squad":
        card = FindCard.find_card(deck[current_index - 1], card_array, cards_dict)
        print(deck[current_index - 1])
        if card.check_for_a_trait("Pledge"):
            current_index = 5
            if card.get_name() == "Holy Crusade":
                holy_crusade_relevant = True
        else:
            return "Non-Pledge card in Pledge position"
    while deck[current_index] != "Army":
        if deck[current_index] in remaining_signature_squad:
            print("Found a match")
            try:
                remaining_signature_squad.remove(deck[current_index])
            except ValueError:
                print("How?")
            print(remaining_signature_squad)
        else:
            print("No match")
            return "Unexpected Card in Signature Squad: " + deck[current_index]
        current_index += 1
    if len(remaining_signature_squad) > 0:
        return "Missing something from signature squad"
    synapse_needed = False
    has_synapse = False
    if factions[0] == "Tyranids":
        synapse_needed = True
    current_index += 1
    card_count = 0
    skippers = ["Support", "Attachment", "Event", "Synapse"]
    while deck[current_index] != "Planet" and current_index < len(deck):
        if len(deck[current_index]) > 3:
            current_name = deck[current_index][3:]
            current_amount = deck[current_index][0]
            try:
                card_count += int(current_amount)
                if int(current_amount) > 3:
                    print("Too many copies")
                    return "Too many copies: " + current_name
            except ValueError:
                return "Number missing"
            card_result = FindCard.find_card(current_name, card_array, cards_dict)
            if card_result.get_name() != current_name:
                print("Card not found in database", current_name)
                return "Card not found in database: " + current_name
            if card_result.get_loyalty() == "Signature":
                print("Signature card found")
                return "Signature card found: " + current_name
            if card_result.get_card_type() == "Synapse":
                if synapse_needed:
                    if has_synapse:
                        return "Too many Synapse units given"
                    else:
                        if current_amount != "1":
                            return "Wrong number for synapse unit"
                        has_synapse = True
                        card_count = card_count - 1
                else:
                    return "Synapse units not allowed in this deck"
            faction_check_passed = False
            if holy_crusade_relevant:
                if not card_result.check_for_a_trait("Ecclesiarchy"):
                    return "Non-Ecclesiarchy card present: " + card_result.get_name()
            if card_result.get_faction() == factions[0]:
                faction_check_passed = True
            elif card_result.get_faction() == factions[1] and card_result.get_loyalty() == "Common":
                if warlord == "Yvraine":
                    if card_result.get_faction() == "Chaos" and card_result.check_for_a_trait("Elite"):
                        return 'Yvraine cannot have Chaos elites: ' + card_result.get_name()
                faction_check_passed = True
            elif card_result.get_faction() != factions[0] and card_result.get_loyalty() == "Loyal":
                return "Loyal card detected: " + card_result.get_name()
            elif factions[0] == "Necrons" and card_result.get_faction() != "Tyranids" and \
                    card_result.get_loyalty() == "Common" and card_result.get_card_type() == "Army":
                faction_check_passed = True
            elif card_result.get_faction() == "Neutral":
                if factions[0] == "Tyranids" and card_result.get_card_type() == "Army":
                    return "Tyranids may not have Neutral Army Units in their deck"
                faction_check_passed = True
            elif warlord == "Gorzod":
                if card_result.get_faction() == "Astra Militarum" or card_result.get_faction() == "Space Marines":
                    if card_result.get_card_type() == "Army" and card_result.get_loyalty() == "Common":
                        if card_result.check_for_a_trait("Vehicle"):
                            faction_check_passed = True
            if not faction_check_passed:
                print("Faction check not passed", factions[0], factions[1], card_result.get_faction())
                return "Faction check not passed (Main, Ally, Card): " \
                       + factions[0] + ", " + factions[1] + ", " + card_result.get_faction()
        current_index += 1
        while deck[current_index] in skippers:
            current_index += 1
    if synapse_needed and not has_synapse:
        return "No Synapse Unit Given"
    if card_count < 42:
        print("Too few cards")
        print(card_count)
        return "Too few cards: " + str(card_count + 8)
    print("No issues")
    return "SUCCESS"


def get_published_decks_lists():
    deck_names = []
    deck_warlords = []
    deck_dates = []
    img_srcs = []
    keys = []
    creator_name = []
    directory = os.getcwd()
    target_directory = directory + "/decks/publisheddecks/"
    if os.path.exists(target_directory):
        for creator in os.listdir(target_directory):
            for file in os.listdir(target_directory + "/" + creator):
                try:
                    target_file = target_directory + "/" + creator + "/" + file
                    with open(target_file + "/content", "r") as f:
                        data = f.read()
                        split_data = data.split(sep="\n")
                        deck_name = split_data[0]
                        warlord_name = split_data[2]
                        timestamp = os.path.getmtime(target_file + "/key")
                        datestamp = datetime.datetime.fromtimestamp(timestamp)
                        date = str(datestamp.date())
                        deck_names.append(deck_name)
                        creator_name.append(creator)
                        deck_warlords.append(warlord_name)
                        deck_dates.append(date)
                        img_src = convert_name_to_img_src(warlord_name)
                        img_srcs.append(img_src)
                        f.close()
                    with open(target_file + "/key", "r") as k:
                        data = k.read()
                        keys.append(data)
                except Exception as e:
                    print(e)
                    pass
    return deck_names, deck_warlords, deck_dates, img_srcs, keys, creator_name

# Views start here


def decks(request):
    deck_names, deck_warlords, deck_dates, img_srcs, keys, creator_name = get_published_decks_lists()
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    data = {
        "Deck Names": deck_names,
        "Deck Warlords": deck_warlords,
        "Deck Dates": deck_dates,
        "Img Srcs": img_srcs,
        "Keys": keys,
        "Creator Name": creator_name
    }
    try:
        df = pd.DataFrame(data=data)
        df = df.sort_values(by="Deck Dates", ascending=False)
        new_deck_names = df["Deck Names"]
        new_deck_warlords = df["Deck Warlords"]
        new_deck_dates = df["Deck Dates"]
        new_img_srcs = df["Img Srcs"]
        new_keys = df["Keys"]
        new_creator_name = df["Creator Name"]
        decks_var = zip(new_deck_names[0:1], new_deck_warlords[0:1], new_deck_dates[0:1],
                        new_img_srcs[0:1], new_keys[0:1], new_creator_name[0:1])

        return render(request, "decks/home_decks.html", {"decks_exist": "Yes", "decks": decks_var,
                                                         "light_dark_toggle": light_dark_toggle})
    except Exception as e:
        print(e)
    return render(request, "decks/home_decks.html", {"decks_exist": "No", "light_dark_toggle": light_dark_toggle})


def delete_deck(request, deck_key):
    print("delete deck")
    delete_private_deck(deck_key, request.user.username)
    return HttpResponseRedirect('/decks/my_decks/')


def retract_deck(request, deck_key):
    print("delete deck")
    delete_published_deck(deck_key, request.user.username)
    return HttpResponseRedirect('/decks/my_decks/')


def published_decks_page(request, page_num):
    smallest_deck_num = (page_num - 1) * 10
    largest_deck_num = page_num * 10
    decks_var = zip([], [], [], [], [], [])
    deck_names, deck_warlords, deck_dates, img_srcs, keys, creator_name = get_published_decks_lists()
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    data = {
        "Deck Names": deck_names,
        "Deck Warlords": deck_warlords,
        "Deck Dates": deck_dates,
        "Img Srcs": img_srcs,
        "Keys": keys,
        "Creator Name": creator_name
    }
    try:
        df = pd.DataFrame(data=data)
        df = df.sort_values(by="Deck Dates", ascending=False)
        new_deck_names = df["Deck Names"]
        if len(new_deck_names) < smallest_deck_num:
            return render(request, "decks/published_decks.html",
                          {"decks": decks_var, "light_dark_toggle": light_dark_toggle})
        if len(new_deck_names) <= largest_deck_num:
            largest_deck_num = len(new_deck_names)
        new_deck_names = new_deck_names[smallest_deck_num:largest_deck_num]
        new_deck_warlords = df["Deck Warlords"]
        new_deck_warlords = new_deck_warlords[smallest_deck_num:largest_deck_num]
        new_deck_dates = df["Deck Dates"]
        new_deck_dates = new_deck_dates[smallest_deck_num:largest_deck_num]
        new_img_srcs = df["Img Srcs"]
        new_img_srcs = new_img_srcs[smallest_deck_num:largest_deck_num]
        new_keys = df["Keys"]
        new_keys = new_keys[smallest_deck_num:largest_deck_num]
        new_creator_name = df["Creator Name"]
        new_creator_name = new_creator_name[smallest_deck_num:largest_deck_num]
        decks_var = zip(new_deck_names, new_deck_warlords, new_deck_dates,
                        new_img_srcs, new_keys, new_creator_name)
        return render(request, "decks/published_decks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})
    except Exception as e:
        print(e)
    return render(request, "decks/published_decks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})


def published_decks(request):
    deck_names, deck_warlords, deck_dates, img_srcs, keys, creator_name = get_published_decks_lists()
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    data = {
        "Deck Names": deck_names,
        "Deck Warlords": deck_warlords,
        "Deck Dates": deck_dates,
        "Img Srcs": img_srcs,
        "Keys": keys,
        "Creator Name": creator_name
    }
    try:
        df = pd.DataFrame(data=data)
        df = df.sort_values(by="Deck Dates", ascending=False)
        new_deck_names = df["Deck Names"]
        new_deck_warlords = df["Deck Warlords"]
        new_deck_dates = df["Deck Dates"]
        new_img_srcs = df["Img Srcs"]
        new_keys = df["Keys"]
        new_creator_name = df["Creator Name"]
        decks_var = zip(new_deck_names, new_deck_warlords, new_deck_dates,
                        new_img_srcs, new_keys, new_creator_name)
        return render(request, "decks/published_decks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})
    except Exception as e:
        print(e)
    decks_var = zip(deck_names, deck_warlords, deck_dates, img_srcs, keys, creator_name)
    return render(request, "decks/published_decks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})


def my_decks_page(request, page_num):
    smallest_deck_num = (page_num - 1) * 10
    largest_deck_num = page_num * 10
    deck_names = []
    deck_warlords = []
    deck_dates = []
    img_srcs = []
    keys = []
    decks_var = zip([], [], [], [], [])
    username = request.user.username
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/" + username + "/"
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    if username:
        if os.path.exists(target_directory):
            for file in os.listdir(target_directory):
                try:
                    target_file = target_directory + file
                    with open(target_file + "/content", "r") as f:
                        data = f.read()
                        split_data = data.split(sep="\n")
                        deck_name = split_data[0]
                        warlord_name = split_data[2]
                        timestamp = os.path.getmtime(target_file + "/key")
                        datestamp = datetime.datetime.fromtimestamp(timestamp)
                        date = str(datestamp.date())
                        deck_names.append(deck_name)
                        deck_warlords.append(warlord_name)
                        deck_dates.append(date)
                        img_src = convert_name_to_img_src(warlord_name)
                        img_srcs.append(img_src)
                        f.close()
                    if not os.path.exists(target_file + "/key"):
                        num_tries = 0
                        set_key = False
                        while not set_key:
                            new_key = ''.join(random.choice(
                                string.ascii_uppercase + string.ascii_lowercase + string.digits
                            ) for _ in range(16 + num_tries))
                            print(new_key)
                            if not check_if_key_in_use(new_key):
                                with open(target_file + "/key", "w") as file:
                                    file.write(new_key)
                                set_key = True
                            if num_tries > 100:
                                with open(target_file + "/key", "w") as file:
                                    file.write(new_key)
                                    set_key = True
                            num_tries += 1
                    with open(target_file + "/key", "r") as k:
                        data = k.read()
                        keys.append(data)
                except Exception as e:
                    print(e)
                    pass
    data = {
        "Deck Names": deck_names,
        "Deck Warlords": deck_warlords,
        "Deck Dates": deck_dates,
        "Img Srcs": img_srcs,
        "Keys": keys
    }
    try:
        df = pd.DataFrame(data=data)
        df = df.sort_values(by="Deck Dates", ascending=False)
        new_deck_names = df["Deck Names"]
        if len(new_deck_names) < smallest_deck_num:
            return render(request, "decks/mydecks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})
        if len(new_deck_names) <= largest_deck_num:
            largest_deck_num = len(new_deck_names)
        new_deck_names = new_deck_names[smallest_deck_num:largest_deck_num]
        new_deck_warlords = df["Deck Warlords"]
        new_deck_warlords = new_deck_warlords[smallest_deck_num:largest_deck_num]
        new_deck_dates = df["Deck Dates"]
        new_deck_dates = new_deck_dates[smallest_deck_num:largest_deck_num]
        new_img_srcs = df["Img Srcs"]
        new_img_srcs = new_img_srcs[smallest_deck_num:largest_deck_num]
        new_keys = df["Keys"]
        new_keys = new_keys[smallest_deck_num:largest_deck_num]
        decks_var = zip(new_deck_names, new_deck_warlords, new_deck_dates, new_img_srcs, new_keys)
        return render(request, "decks/mydecks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})
    except Exception as e:
        print(e)
    return render(request, "decks/mydecks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})


def my_published_decks_page(request, page_num):
    smallest_deck_num = (page_num - 1) * 10
    largest_deck_num = page_num * 10
    deck_names = []
    deck_warlords = []
    deck_dates = []
    img_srcs = []
    keys = []
    decks_var = zip([], [], [], [], [])
    username = request.user.username
    directory = os.getcwd()
    target_directory = directory + "/decks/publisheddecks/" + username + "/"
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    if username:
        if os.path.exists(target_directory):
            for file in os.listdir(target_directory):
                try:
                    target_file = target_directory + file
                    with open(target_file + "/content", "r") as f:
                        data = f.read()
                        split_data = data.split(sep="\n")
                        deck_name = split_data[0]
                        warlord_name = split_data[2]
                        timestamp = os.path.getmtime(target_file + "/key")
                        datestamp = datetime.datetime.fromtimestamp(timestamp)
                        date = str(datestamp.date())
                        deck_names.append(deck_name)
                        deck_warlords.append(warlord_name)
                        deck_dates.append(date)
                        img_src = convert_name_to_img_src(warlord_name)
                        img_srcs.append(img_src)
                        f.close()
                    if not os.path.exists(target_file + "/key"):
                        num_tries = 0
                        set_key = False
                        while not set_key:
                            new_key = ''.join(random.choice(
                                string.ascii_uppercase + string.ascii_lowercase + string.digits
                            ) for _ in range(16 + num_tries))
                            print(new_key)
                            if not check_if_key_in_use(new_key):
                                with open(target_file + "/key", "w") as file:
                                    file.write(new_key)
                                set_key = True
                            if num_tries > 100:
                                with open(target_file + "/key", "w") as file:
                                    file.write(new_key)
                                    set_key = True
                            num_tries += 1
                    with open(target_file + "/key", "r") as k:
                        data = k.read()
                        keys.append(data)
                except Exception as e:
                    print(e)
                    pass
    data = {
        "Deck Names": deck_names,
        "Deck Warlords": deck_warlords,
        "Deck Dates": deck_dates,
        "Img Srcs": img_srcs,
        "Keys": keys
    }
    try:
        df = pd.DataFrame(data=data)
        df = df.sort_values(by="Deck Dates", ascending=False)
        new_deck_names = df["Deck Names"]
        if len(new_deck_names) < smallest_deck_num:
            return render(request, "decks/my_published_decks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})
        if len(new_deck_names) <= largest_deck_num:
            largest_deck_num = len(new_deck_names)
        new_deck_names = new_deck_names[smallest_deck_num:largest_deck_num]
        new_deck_warlords = df["Deck Warlords"]
        new_deck_warlords = new_deck_warlords[smallest_deck_num:largest_deck_num]
        new_deck_dates = df["Deck Dates"]
        new_deck_dates = new_deck_dates[smallest_deck_num:largest_deck_num]
        new_img_srcs = df["Img Srcs"]
        new_img_srcs = new_img_srcs[smallest_deck_num:largest_deck_num]
        new_keys = df["Keys"]
        new_keys = new_keys[smallest_deck_num:largest_deck_num]
        decks_var = zip(new_deck_names, new_deck_warlords, new_deck_dates, new_img_srcs, new_keys)
        return render(request, "decks/my_published_decks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})
    except Exception as e:
        print(e)
    return render(request, "decks/my_published_decks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})


def my_published_decks(request):
    deck_names = []
    deck_warlords = []
    deck_dates = []
    img_srcs = []
    keys = []
    username = request.user.username
    directory = os.getcwd()
    target_directory = directory + "/decks/publisheddecks/" + username + "/"
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    if username:
        if os.path.exists(target_directory):
            for file in os.listdir(target_directory):
                try:
                    target_file = target_directory + file
                    with open(target_file + "/content", "r") as f:
                        data = f.read()
                        split_data = data.split(sep="\n")
                        deck_name = split_data[0]
                        warlord_name = split_data[2]
                        timestamp = os.path.getmtime(target_file + "/key")
                        datestamp = datetime.datetime.fromtimestamp(timestamp)
                        date = str(datestamp.date())
                        deck_names.append(deck_name)
                        deck_warlords.append(warlord_name)
                        deck_dates.append(date)
                        img_src = convert_name_to_img_src(warlord_name)
                        img_srcs.append(img_src)
                        f.close()
                    if not os.path.exists(target_file + "/key"):
                        num_tries = 0
                        set_key = False
                        while not set_key:
                            new_key = ''.join(random.choice(
                                string.ascii_uppercase + string.ascii_lowercase + string.digits
                            ) for _ in range(16 + num_tries))
                            print(new_key)
                            if not check_if_key_in_use(new_key):
                                with open(target_file + "/key", "w") as file:
                                    file.write(new_key)
                                set_key = True
                            if num_tries > 100:
                                with open(target_file + "/key", "w") as file:
                                    file.write(new_key)
                                    set_key = True
                            num_tries += 1
                    with open(target_file + "/key", "r") as k:
                        data = k.read()
                        keys.append(data)
                except Exception as e:
                    print(e)
                    pass
    data = {
        "Deck Names": deck_names,
        "Deck Warlords": deck_warlords,
        "Deck Dates": deck_dates,
        "Img Srcs": img_srcs,
        "Keys": keys
    }
    try:
        df = pd.DataFrame(data=data)
        df = df.sort_values(by="Deck Dates", ascending=False)
        new_deck_names = df["Deck Names"]
        new_deck_warlords = df["Deck Warlords"]
        new_deck_dates = df["Deck Dates"]
        new_img_srcs = df["Img Srcs"]
        new_keys = df["Keys"]
        decks_var = zip(new_deck_names, new_deck_warlords, new_deck_dates, new_img_srcs, new_keys)
        return render(request, "decks/my_published_decks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})
    except Exception as e:
        print(e)
    decks_var = zip(deck_names, deck_warlords, deck_dates, img_srcs, keys)
    return render(request, "decks/my_published_decks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})


def my_decks(request):
    deck_names = []
    deck_warlords = []
    deck_dates = []
    img_srcs = []
    keys = []
    username = request.user.username
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/" + username + "/"
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    if username:
        if os.path.exists(target_directory):
            for file in os.listdir(target_directory):
                try:
                    target_file = target_directory + file
                    with open(target_file + "/content", "r") as f:
                        data = f.read()
                        split_data = data.split(sep="\n")
                        deck_name = split_data[0]
                        warlord_name = split_data[2]
                        timestamp = os.path.getmtime(target_file + "/key")
                        datestamp = datetime.datetime.fromtimestamp(timestamp)
                        date = str(datestamp.date())
                        deck_names.append(deck_name)
                        deck_warlords.append(warlord_name)
                        deck_dates.append(date)
                        img_src = convert_name_to_img_src(warlord_name)
                        img_srcs.append(img_src)
                        f.close()
                    if not os.path.exists(target_file + "/key"):
                        num_tries = 0
                        set_key = False
                        while not set_key:
                            new_key = ''.join(random.choice(
                                string.ascii_uppercase + string.ascii_lowercase + string.digits
                            ) for _ in range(16 + num_tries))
                            print(new_key)
                            if not check_if_key_in_use(new_key):
                                with open(target_file + "/key", "w") as file:
                                    file.write(new_key)
                                set_key = True
                            if num_tries > 100:
                                with open(target_file + "/key", "w") as file:
                                    file.write(new_key)
                                    set_key = True
                            num_tries += 1
                    with open(target_file + "/key", "r") as k:
                        data = k.read()
                        keys.append(data)
                except Exception as e:
                    print(e)
                    pass
    data = {
        "Deck Names": deck_names,
        "Deck Warlords": deck_warlords,
        "Deck Dates": deck_dates,
        "Img Srcs": img_srcs,
        "Keys": keys
    }
    try:
        df = pd.DataFrame(data=data)
        df = df.sort_values(by="Deck Dates", ascending=False)
        new_deck_names = df["Deck Names"]
        new_deck_warlords = df["Deck Warlords"]
        new_deck_dates = df["Deck Dates"]
        new_img_srcs = df["Img Srcs"]
        new_keys = df["Keys"]
        decks_var = zip(new_deck_names, new_deck_warlords, new_deck_dates, new_img_srcs, new_keys)
        return render(request, "decks/mydecks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})
    except Exception as e:
        print(e)
    decks_var = zip(deck_names, deck_warlords, deck_dates, img_srcs, keys)
    return render(request, "decks/mydecks.html", {"decks": decks_var, "light_dark_toggle": light_dark_toggle})


def modify_deck(request, deck_key):
    username = request.user.username
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/" + username + "/"
    data = []
    desc = ""
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    if username:
        if os.path.exists(target_directory):
            for file in os.listdir(target_directory):
                target_file = target_directory + file
                with open(target_file + "/key", "r") as k:
                    current_key = k.read()
                    if current_key == deck_key:
                        with open(target_file + "/content", "r") as f:
                            data = f.read().replace("\n", "|||")
                        with open(target_file + "/desc", "r") as f:
                            desc = f.read()
    if data:
        return render(request, "decks/createdeck.html", {"edit": "T", "data": data, "desc": desc,
                                                         "auto_complete": card_names_array,
                                                         "warlord_name": "", "warlord_sig": [],
                                                         "warlord_src": "",
                                                         "light_dark_toggle": light_dark_toggle})
    return render(request, "decks/createdeck.html", {"edit": "F", "data": "", "desc": "",
                                                     "auto_complete": card_names_array,
                                                     "warlord_name": "", "warlord_sig": [],
                                                     "warlord_src": "",
                                                     "light_dark_toggle": light_dark_toggle})


def create_deck(request):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    return render(request, "decks/createdeck.html", {"edit": "F", "data": "", "desc": "",
                                                     "auto_complete": card_names_array,
                                                     "warlord_name": "", "warlord_sig": [],
                                                     "warlord_src": "",
                                                     "light_dark_toggle": light_dark_toggle})


def create_deck_with_warlord(request, warlord_name):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    try:
        actual_name = warlord_name.replace("_", " ")
        if actual_name in cards_dict:
            warlord_card = cards_dict[actual_name]
            if warlord_card.get_card_type() == "Warlord":
                warlord_faction = warlord_card.get_faction()
                warlord_sig = warlord_card.signature_squad
                warlord_src = convert_name_to_img_src(actual_name)
                return render(request, "decks/createdeck.html", {"edit": "F", "data": "", "desc": "",
                                                                 "auto_complete": card_names_array,
                                                                 "warlord_name": warlord_name,
                                                                 "warlord_sig": warlord_sig,
                                                                 "warlord_src": warlord_faction,
                                                                 "light_dark_toggle": light_dark_toggle})
    except Exception as e:
        print(e)
    return render(request, "decks/createdeck.html", {"edit": "F", "data": "", "desc": "",
                                                     "auto_complete": card_names_array,
                                                     "warlord_name": "", "warlord_sig": [],
                                                     "warlord_src": "",
                                                     "light_dark_toggle": light_dark_toggle})


def user_deck_data(request, deck_creator):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    return render(request, "decks/user_deck_data.html", {"light_dark_toggle": light_dark_toggle})


def advanced_deck_details(request, deck_creator, deck_key):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    deck_found = "N"
    username = request.user.username
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/" + deck_creator + "/"
    permitted_to_read = False
    public_deck = "F"
    stored_target_file = ""
    if os.path.exists(target_directory):
        for file in os.listdir(target_directory):
            try:
                target_file = target_directory + file
                with open(target_file + "/key", "r") as f:
                    data = f.read()
                    if data == deck_key:
                        if username == deck_creator:
                            permitted_to_read = True
                            stored_target_file = target_file
            except Exception as e:
                print(e)
                pass
    if not permitted_to_read:
        target_directory = directory + "/decks/publisheddecks/" + deck_creator + "/"
        if os.path.exists(target_directory):
            for file in os.listdir(target_directory):
                try:
                    target_file = target_directory + file
                    with open(target_file + "/key", "r") as f:
                        data = f.read()
                        if data == deck_key:
                            print("key match")
                            permitted_to_read = True
                            stored_target_file = target_file
                            public_deck = "T"
                            if username == deck_creator:
                                public_deck = "OWNER"
                except Exception as e:
                    print(e)
    if permitted_to_read:
        deck_found = "Y"
        with open(stored_target_file + "/content", "r") as f:
            deck_content = f.read()
        with open(stored_target_file + "/desc", "r") as f:
            description = f.read()
        deck_list = deck_content.split(sep="\n")
        deck_list = list(filter(("----------------------------------------------------------------------").__ne__,
                                deck_list))
        deck_list = list(filter(("Planet").__ne__, deck_list))
        deck_list = list(filter(("").__ne__, deck_list))
        deck_name = deck_list[0]
        warlord_name = deck_list[1]
        factions = deck_list[2]
        sig_pos = -1
        army_pos = -1
        support_pos = -1
        attachment_pos = -1
        event_pos = -1
        synapse_pos = -1
        extra_army_cards = 0
        extra_support_cards = 0
        extra_attachment_cards = 0
        extra_event_cards = 0
        army_card_count = 0
        support_card_count = 0
        event_card_count = 0
        attachment_card_count = 0
        synapse_name = ""
        pledge_name = ""
        last_card_type = ""
        for i in range(len(deck_list)):
            if deck_list[i] == "Signature Squad":
                sig_pos = i
                last_card_type = deck_list[i]
                if deck_list[i - 1] in pledges_array:
                    pledge_name = deck_list[i - 1]
            elif deck_list[i] == "Army":
                army_pos = i
                last_card_type = deck_list[i]
            elif deck_list[i] == "Support":
                support_pos = i
                last_card_type = deck_list[i]
            elif deck_list[i] == "Event":
                event_pos = i
                last_card_type = deck_list[i]
            elif deck_list[i] == "Attachment":
                attachment_pos = i
                last_card_type = deck_list[i]
            elif deck_list[i] == "Synapse":
                last_card_type = deck_list[i]
                if deck_list[i + 1] != "Attachment":
                    synapse_name = deck_list[i + 1]
                synapse_pos = i
            elif last_card_type != "Synapse" and deck_list[i]:
                if last_card_type == "Signature Squad":
                    card_name = deck_list[i][3:]
                    card = FindCard.find_card(card_name, card_array, cards_dict)
                    print(card.get_name())
                    if card.get_card_type() == "Army":
                        extra_army_cards += int(deck_list[i][0])
                    if card.get_card_type() == "Event":
                        extra_event_cards += int(deck_list[i][0])
                    if card.get_card_type() == "Attachment":
                        extra_attachment_cards += int(deck_list[i][0])
                    if card.get_card_type() == "Support":
                        extra_support_cards += int(deck_list[i][0])
                elif last_card_type == "Army":
                    army_card_count += int(deck_list[i][0])
                elif last_card_type == "Support":
                    support_card_count += int(deck_list[i][0])
                elif last_card_type == "Event":
                    event_card_count += int(deck_list[i][0])
                elif last_card_type == "Attachment":
                    attachment_card_count += int(deck_list[i][0])
        print(attachment_card_count)
        print(army_card_count)
        print(extra_event_cards)
        sig_cards = deck_list[sig_pos + 1:army_pos]
        army_cards = deck_list[army_pos + 1:support_pos]
        support_cards = deck_list[support_pos + 1:synapse_pos]
        attachment_cards = deck_list[attachment_pos + 1:event_pos]
        event_cards = deck_list[event_pos + 1:]
        warlord_img = convert_name_to_img_src(warlord_name)
        warlord_link = convert_name_to_hyperlink(warlord_name)
        synapse_img = "None"
        synapse_link = "None"
        pledge_img = "None"
        pledge_link = "None"
        if synapse_name:
            synapse_img = convert_name_to_img_src(synapse_name[3:])
            synapse_link = convert_name_to_hyperlink(synapse_name[3:])
        if pledge_name:
            pledge_img = convert_name_to_img_src(pledge_name)
            pledge_link = convert_name_to_hyperlink(pledge_name)
        print(sig_cards)
        print(army_cards)
        print(support_cards)
        print(attachment_cards)
        print(event_cards)
        links_to_sig_cards = []
        links_to_army_cards = []
        links_to_support_cards = []
        links_to_attachment_cards = []
        links_to_event_cards = []
        sig_srcs = []
        army_srcs = []
        support_srcs = []
        attachment_srcs = []
        event_srcs = []
        cost_indices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        cost_values = [0 for _ in range(11)]
        for card_name in sig_cards:
            actual_name = card_name[3:]
            links_to_sig_cards.append(convert_name_to_hyperlink(actual_name))
            sig_srcs.append(convert_name_to_img_src(actual_name))
            cost = FindCard.find_card(actual_name, card_array, cards_dict).get_cost()
            if cost != -1 and cost < 11:
                try:
                    str_cost = str(cost)
                    if str_cost in cost_indices:
                        cost_values[cost] += int(card_name[0])
                except:
                    pass
        for card_name in army_cards:
            actual_name = card_name[3:]
            links_to_army_cards.append(convert_name_to_hyperlink(actual_name))
            army_srcs.append(convert_name_to_img_src(actual_name))
            cost = FindCard.find_card(actual_name, card_array, cards_dict).get_cost()
            if cost != -1 and cost < 11:
                try:
                    str_cost = str(cost)
                    if str_cost in cost_indices:
                        cost_values[cost] += int(card_name[0])
                except:
                    pass
        for card_name in support_cards:
            actual_name = card_name[3:]
            links_to_support_cards.append(convert_name_to_hyperlink(actual_name))
            support_srcs.append(convert_name_to_img_src(actual_name))
            cost = FindCard.find_card(actual_name, card_array, cards_dict).get_cost()
            if cost != -1 and cost < 11:
                try:
                    str_cost = str(cost)
                    if str_cost in cost_indices:
                        cost_values[cost] += int(card_name[0])
                except:
                    pass
        for card_name in attachment_cards:
            actual_name = card_name[3:]
            links_to_attachment_cards.append(convert_name_to_hyperlink(actual_name))
            attachment_srcs.append(convert_name_to_img_src(actual_name))
            cost = FindCard.find_card(actual_name, card_array, cards_dict).get_cost()
            if cost != -1 and cost < 11:
                try:
                    str_cost = str(cost)
                    if str_cost in cost_indices:
                        cost_values[cost] += int(card_name[0])
                except:
                    pass
        for card_name in event_cards:
            actual_name = card_name[3:]
            links_to_event_cards.append(convert_name_to_hyperlink(actual_name))
            event_srcs.append(convert_name_to_img_src(actual_name))
            cost = FindCard.find_card(actual_name, card_array, cards_dict).get_cost()
            if cost != -1 and cost < 11:
                try:
                    str_cost = str(cost)
                    if str_cost in cost_indices:
                        cost_values[cost] += int(card_name[0])
                except:
                    pass
        raw_card_data = [*sig_cards, *army_cards, *support_cards, *attachment_cards, *event_cards]
        sig_cards = zip(sig_cards, links_to_sig_cards, sig_srcs)
        army_cards = zip(army_cards, links_to_army_cards, army_srcs)
        support_cards = zip(support_cards, links_to_support_cards, support_srcs)
        attachment_cards = zip(attachment_cards, links_to_attachment_cards, attachment_srcs)
        event_cards = zip(event_cards, links_to_event_cards, event_srcs)
        names_comments = []
        times_comments = []
        comments = []
        comment_ids = []
        no_comments = True
        target_directory = directory + "/decks/comments/" + deck_key + "/"
        if request.method == 'POST':
            flag = request.POST.get('flag')
            if flag == "POST":
                username = request.POST.get('username')
                if not username:
                    username = "Anonymous"
                comment = request.POST.get('comment')
                time = str(datetime.datetime.now())
                os.makedirs(target_directory, exist_ok=True)
                file_id = len(
                    [name for name in os.listdir(target_directory) if os.path.isfile(target_directory + "/" + name)])
                name_file = str(file_id) + ".txt"
                with open(target_directory + name_file, 'w') as file:
                    file.write(username + "\n" + time + "\n" + comment)
            elif flag == "DELETE":
                # username = request.POST.get('username')
                id_c = request.POST.get('idcomment')
                name_file = id_c + ".txt"
                with open(target_directory + name_file, 'w') as file:
                    file.write("")
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
        deck_content = deck_content.replace("\n", "|||")
        return render(request, "decks/advanced_deck_details.html",
                      {"deck_found": deck_found, "deck_content": deck_content,
                       "description": description, "deck_list": deck_list,
                       "factions": factions, "deck_name": deck_name,
                       "sig_cards": sig_cards, "army_cards": army_cards,
                       "support_cards": support_cards,
                       "attachment_cards": attachment_cards,
                       "event_cards": event_cards,
                       "warlord_img": warlord_img, "synapse_img": synapse_img,
                       "warlord_link": warlord_link, "synapse_link": synapse_link,
                       "creator": deck_creator, "public": public_deck,
                       "deck_key": deck_key,
                       "comments": my_comments, "noc": no_comments,
                       "pledge_img": pledge_img, "pledge_link": pledge_link,
                       "light_dark_toggle": light_dark_toggle,
                       "event_card_count": event_card_count,
                       "extra_event_cards": extra_event_cards,
                       "army_card_count": army_card_count,
                       "extra_army_cards": extra_army_cards,
                       "attachment_card_count": attachment_card_count,
                       "extra_attachment_cards": extra_attachment_cards,
                       "support_card_count": support_card_count,
                       "extra_support_cards": extra_support_cards,
                       "cards_raw": raw_card_data, "cost_indices": cost_indices,
                       "cost_values": cost_values}
                      )
    return render(request, "decks/advanced_deck_details.html",
                  {"deck_found": deck_found, "deck_content": "", "light_dark_toggle": light_dark_toggle,
                   "cards_raw": []})


def deck_data(request, deck_creator, deck_key):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    deck_found = "N"
    username = request.user.username
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/" + deck_creator + "/"
    permitted_to_read = False
    public_deck = "F"
    liked = False
    like_count = 0
    stored_target_file = ""
    if os.path.exists(target_directory):
        for file in os.listdir(target_directory):
            try:
                target_file = target_directory + file
                with open(target_file + "/key", "r") as f:
                    data = f.read()
                    if data == deck_key:
                        if username == deck_creator:
                            permitted_to_read = True
                            stored_target_file = target_file
            except Exception as e:
                print(e)
                pass
    if not permitted_to_read:
        target_directory = directory + "/decks/publisheddecks/" + deck_creator + "/"
        if os.path.exists(target_directory):
            for file in os.listdir(target_directory):
                try:
                    target_file = target_directory + file
                    with open(target_file + "/key", "r") as f:
                        data = f.read()
                        if data == deck_key:
                            permitted_to_read = True
                            stored_target_file = target_file
                            public_deck = "T"
                            if username == deck_creator:
                                public_deck = "OWNER"
                            if not os.path.exists(target_file + "/likes"):
                                print("making new file")
                                with open(target_file + "/likes", "w") as like_file:
                                    like_file.write("")
                                    like_file.close()
                            with open(target_file + "/likes") as like_file:
                                content = like_file.read()
                                liked_names = content.split(sep="\n")
                                liked_names = [x for x in liked_names if x]
                                if username:
                                    if username in liked_names:
                                        liked = True
                                if len(liked_names) > 0:
                                    like_count = len(liked_names)
                except Exception as e:
                    print(e)
    if permitted_to_read:
        deck_found = "Y"
        with open(stored_target_file + "/content", "r") as f:
            deck_content = f.read()
        with open(stored_target_file + "/desc", "r") as f:
            description = f.read()
        deck_list = deck_content.split(sep="\n")
        deck_list = list(filter(("----------------------------------------------------------------------").__ne__,
                                deck_list))
        deck_list = list(filter(("Planet").__ne__, deck_list))
        deck_list = list(filter(("").__ne__, deck_list))
        deck_name = deck_list[0]
        warlord_name = deck_list[1]
        factions = deck_list[2]
        sig_pos = -1
        army_pos = -1
        support_pos = -1
        attachment_pos = -1
        event_pos = -1
        synapse_pos = -1
        extra_army_cards = 0
        extra_support_cards = 0
        extra_attachment_cards = 0
        extra_event_cards = 0
        army_card_count = 0
        support_card_count = 0
        event_card_count = 0
        attachment_card_count = 0
        synapse_name = ""
        pledge_name = ""
        last_card_type = ""
        for i in range(len(deck_list)):
            if deck_list[i] == "Signature Squad":
                sig_pos = i
                last_card_type = deck_list[i]
                if deck_list[i - 1] in pledges_array:
                    pledge_name = deck_list[i - 1]
            elif deck_list[i] == "Army":
                army_pos = i
                last_card_type = deck_list[i]
            elif deck_list[i] == "Support":
                support_pos = i
                last_card_type = deck_list[i]
            elif deck_list[i] == "Event":
                event_pos = i
                last_card_type = deck_list[i]
            elif deck_list[i] == "Attachment":
                attachment_pos = i
                last_card_type = deck_list[i]
            elif deck_list[i] == "Synapse":
                last_card_type = deck_list[i]
                if deck_list[i + 1] != "Attachment":
                    synapse_name = deck_list[i + 1]
                synapse_pos = i
            elif last_card_type != "Synapse" and deck_list[i]:
                if last_card_type == "Signature Squad":
                    card_name = deck_list[i][3:]
                    card = FindCard.find_card(card_name, card_array, cards_dict)
                    if card.get_card_type() == "Army":
                        extra_army_cards += int(deck_list[i][0])
                    if card.get_card_type() == "Event":
                        extra_event_cards += int(deck_list[i][0])
                    if card.get_card_type() == "Attachment":
                        extra_attachment_cards += int(deck_list[i][0])
                    if card.get_card_type() == "Support":
                        extra_support_cards += int(deck_list[i][0])
                elif last_card_type == "Army":
                    army_card_count += int(deck_list[i][0])
                elif last_card_type == "Support":
                    support_card_count += int(deck_list[i][0])
                elif last_card_type == "Event":
                    event_card_count += int(deck_list[i][0])
                elif last_card_type == "Attachment":
                    attachment_card_count += int(deck_list[i][0])
        sig_cards = deck_list[sig_pos + 1:army_pos]
        army_cards = deck_list[army_pos + 1:support_pos]
        support_cards = deck_list[support_pos + 1:synapse_pos]
        attachment_cards = deck_list[attachment_pos + 1:event_pos]
        event_cards = deck_list[event_pos + 1:]
        warlord_img = convert_name_to_img_src(warlord_name)
        warlord_link = convert_name_to_hyperlink(warlord_name)
        synapse_img = "None"
        synapse_link = "None"
        pledge_img = "None"
        pledge_link = "None"
        if synapse_name:
            synapse_img = convert_name_to_img_src(synapse_name[3:])
            synapse_link = convert_name_to_hyperlink(synapse_name[3:])
        if pledge_name:
            pledge_img = convert_name_to_img_src(pledge_name)
            pledge_link = convert_name_to_hyperlink(pledge_name)
        links_to_sig_cards = []
        links_to_army_cards = []
        links_to_support_cards = []
        links_to_attachment_cards = []
        links_to_event_cards = []
        sig_srcs = []
        army_srcs = []
        support_srcs = []
        attachment_srcs = []
        event_srcs = []
        for card_name in sig_cards:
            links_to_sig_cards.append(convert_name_to_hyperlink(card_name[3:]))
            sig_srcs.append(convert_name_to_img_src(card_name[3:]))
        for card_name in army_cards:
            links_to_army_cards.append(convert_name_to_hyperlink(card_name[3:]))
            army_srcs.append(convert_name_to_img_src(card_name[3:]))
        for card_name in support_cards:
            links_to_support_cards.append(convert_name_to_hyperlink(card_name[3:]))
            support_srcs.append(convert_name_to_img_src(card_name[3:]))
        for card_name in attachment_cards:
            links_to_attachment_cards.append(convert_name_to_hyperlink(card_name[3:]))
            attachment_srcs.append(convert_name_to_img_src(card_name[3:]))
        for card_name in event_cards:
            links_to_event_cards.append(convert_name_to_hyperlink(card_name[3:]))
            event_srcs.append(convert_name_to_img_src(card_name[3:]))
        sig_cards = zip(sig_cards, links_to_sig_cards, sig_srcs)
        army_cards = zip(army_cards, links_to_army_cards, army_srcs)
        support_cards = zip(support_cards, links_to_support_cards, support_srcs)
        attachment_cards = zip(attachment_cards, links_to_attachment_cards, attachment_srcs)
        event_cards = zip(event_cards, links_to_event_cards, event_srcs)
        names_comments = []
        times_comments = []
        comments = []
        comment_ids = []
        no_comments = True
        target_directory = directory + "/decks/comments/" + deck_key + "/"
        if request.method == 'POST':
            flag = request.POST.get('flag')
            if flag == "POST":
                username = request.POST.get('username')
                if not username:
                    username = "Anonymous"
                comment = request.POST.get('comment')
                time = str(datetime.datetime.now())
                os.makedirs(target_directory, exist_ok=True)
                file_id = len(
                    [name for name in os.listdir(target_directory) if os.path.isfile(target_directory + "/" + name)])
                name_file = str(file_id) + ".txt"
                with open(target_directory + name_file, 'w') as file:
                    file.write(username + "\n" + time + "\n" + comment)
            elif flag == "DELETE":
                # username = request.POST.get('username')
                id_c = request.POST.get('idcomment')
                name_file = id_c + ".txt"
                with open(target_directory + name_file, 'w') as file:
                    file.write("")
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
                        time = datetime.datetime.strptime(split_text[1], '%Y-%m-%d %H:%M:%S.%f')
                        time.replace(microsecond=0)
                        time = time.strftime('%Y-%m-%d %H:%M:%S')
                        times_comments.append(time)
                        comments.append(split_text[2])
                        no_comments = False
        my_comments = zip(names_comments, times_comments, comments, comment_ids)
        deck_content = deck_content.replace("\n", "|||")
        return render(request, "decks/deck_data.html", {"deck_found": deck_found, "deck_content": deck_content,
                                                        "description": description, "deck_list": deck_list,
                                                        "factions": factions, "deck_name": deck_name,
                                                        "sig_cards": sig_cards, "army_cards": army_cards,
                                                        "support_cards": support_cards,
                                                        "attachment_cards": attachment_cards,
                                                        "event_cards": event_cards,
                                                        "warlord_img": warlord_img, "synapse_img": synapse_img,
                                                        "warlord_link": warlord_link, "synapse_link": synapse_link,
                                                        "creator": deck_creator, "public": public_deck,
                                                        "deck_key": deck_key,
                                                        "comments": my_comments, "noc": no_comments,
                                                        "pledge_img": pledge_img, "pledge_link": pledge_link,
                                                        "light_dark_toggle": light_dark_toggle,
                                                        "event_card_count": event_card_count,
                                                        "extra_event_cards": extra_event_cards,
                                                        "army_card_count": army_card_count,
                                                        "extra_army_cards": extra_army_cards,
                                                        "attachment_card_count": attachment_card_count,
                                                        "extra_attachment_cards": extra_attachment_cards,
                                                        "support_card_count": support_card_count,
                                                        "extra_support_cards": extra_support_cards,
                                                        "liked": liked, "like_count": like_count})
    return render(request, "decks/deck_data.html", {"deck_found": deck_found, "deck_content": "",
                                                    "light_dark_toggle": light_dark_toggle})


def copy_published_deck(request, deck_key):
    og_username = request.user.username
    directory = os.getcwd()
    source_directory = directory + "/decks/publisheddecks/"
    target_directory = directory + "/decks/deckstorage/" + og_username + "/"
    os.makedirs(target_directory, exist_ok=True)
    if os.path.exists(source_directory):
        for username in os.listdir(source_directory):
            if username:
                second_source_directory = source_directory + "/" + username
                for file in os.listdir(second_source_directory):
                    try:
                        target_file = second_source_directory + "/" + file
                        found = False
                        with open(target_file + "/key", "r") as f:
                            data = f.read()
                            if data == deck_key:
                                found = True
                        if found:
                            if not os.path.exists(target_directory + file):
                                shutil.copytree(target_file, target_directory + file)
                                new_key = create_new_key()
                                with open(target_directory + file + "/key", "w") as new_f:
                                    new_f.write(new_key)
                                return HttpResponseRedirect('/decks/' + og_username + "/" + new_key + "/")
                    except Exception as e:
                        print(e)
    return HttpResponseRedirect('/decks/my_decks/')


def like_deck(request, deck_key):
    og_username = request.user.username
    if not og_username:
        return HttpResponseRedirect('/decks/published_decks/')
    directory = os.getcwd()
    source_directory = directory + "/decks/publisheddecks/"
    if os.path.exists(source_directory):
        for username in os.listdir(source_directory):
            if username:
                second_source_directory = source_directory + "/" + username
                for file in os.listdir(second_source_directory):
                    try:
                        target_file = second_source_directory + "/" + file
                        found = False
                        with open(target_file + "/key", "r") as f:
                            data = f.read()
                            if data == deck_key:
                                found = True
                                if not os.path.exists(target_file + "/likes"):
                                    with open(target_file + "/likes", "w") as like_file:
                                        like_file.write("")
                                        like_file.close()
                                with open(target_file + "/likes", "r") as like_file:
                                    content = like_file.read()
                                    liked_names = content.split(sep="\n")
                                    liked_names = [x for x in liked_names if x]
                                    if og_username in liked_names:
                                        liked_names.remove(og_username)
                                    else:
                                        liked_names.append(og_username)
                                print(liked_names)
                                new_string = "\n".join(liked_names)
                                with open(target_file + "/likes", "w") as like_file:
                                    like_file.write(new_string)
                                    like_file.close()
                        if found:
                            return HttpResponseRedirect('/decks/' + username + "/" + deck_key + "/")
                    except Exception as e:
                        print(e)
    return HttpResponseRedirect('/decks/my_decks/')


def publish_deck(request, deck_key):
    username = request.user.username
    directory = os.getcwd()
    target_directory = directory + "/decks/publisheddecks/" + username + "/"
    source_directory = directory + "/decks/deckstorage/" + username + "/"
    os.makedirs(target_directory, exist_ok=True)
    for file in os.listdir(source_directory):
        try:
            target_file = source_directory + file
            published_deck = False
            with open(target_file + "/key", "r") as f:
                data = f.read()
                if data == deck_key:
                    if not os.path.exists(target_directory + file):
                        print("Path does not exist")
                        published_deck = True
                        shutil.copytree(target_file, target_directory + file)
                    else:
                        print("already published this deck!")
            num_tries = 0
            set_key = False
            if published_deck:
                while not set_key:
                    new_key = ''.join(random.choice(
                        string.ascii_uppercase + string.ascii_lowercase + string.digits
                    ) for _ in range(16 + num_tries))
                    print(new_key)
                    if not check_if_key_in_use(new_key):
                        with open(target_directory + file + "/key", "w") as key_file:
                            key_file.write(new_key)
                            return HttpResponseRedirect('/decks/' + username + "/" + new_key + "/")
                    if num_tries > 100:
                        with open(target_directory + file + "/key", "w") as key_file:
                            key_file.write(new_key)
                            return HttpResponseRedirect('/decks/' + username + "/" + new_key + "/")
                    num_tries += 1
        except Exception as e:
            print(e)
    return HttpResponseRedirect('/decks/my_decks/')


def select_warlord(request):
    sent_astra_militarum = zip(astra_militarum_warlords, astra_militarum_img_srcs, astra_militarum_hyperlinks)
    sent_space_marines = zip(space_marines_warlords, space_marines_img_srcs, space_marines_hyperlinks)
    sent_tau = zip(tau_warlords, tau_img_srcs, tau_hyperlinks)
    sent_eldar = zip(eldar_warlords, eldar_img_srcs, eldar_hyperlinks)
    sent_dark_eldar = zip(dark_eldar_warlords, dark_eldar_img_srcs, dark_eldar_hyperlinks)
    sent_chaos = zip(chaos_warlords, chaos_img_srcs, chaos_hyperlinks)
    sent_orks = zip(orks_warlords, orks_img_srcs, orks_hyperlinks)
    sent_tyranids = zip(tyranids_warlords, tyranids_img_srcs, tyranids_hyperlinks)
    sent_necrons = zip(necrons_warlords, necrons_img_srcs, necrons_hyperlinks)
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    return render(request, "decks/select_warlord.html",
                  {"light_dark_toggle": light_dark_toggle,
                   "astra_militarum": sent_astra_militarum, "space_marines": sent_space_marines,
                   "tau": sent_tau, "eldar": sent_eldar, "dark_eldar": sent_dark_eldar,
                   "chaos": sent_chaos, "orks": sent_orks, "tyranids": sent_tyranids, "necrons": sent_necrons})


def ajax_view(request):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        if flag == "SENDDECK":
            text = request.POST.get('deck_text')
            username = request.POST.get('username')
            if username == "":
                username = "Anonymous"
            description = request.POST.get('description')
            force_send = request.POST.get('force_send')
            message_to_send = ""
            text = text.replace("\"Subject: &Omega;-X62113\"", "")
            # text = text.replace("idden Base", "'idden Base")
            text = text.replace("\"", "")
            deck = clean_sent_deck(text)
            print(deck)
            deck_name = deck[0]
            if len(deck) > 5:
                if "{AUTOMAIN}" in deck[2]:
                    warlord = FindCard.find_card(deck[1], card_array, cards_dict)
                    deck[2] = deck[2].replace("{AUTOMAIN}", warlord.get_faction())
                    text = text.replace("{AUTOMAIN}", warlord.get_faction())
                message_to_send = second_part_deck_validation(deck)
            if message_to_send == "SUCCESS":
                print("Need to save deck")
                print(os.getcwd())
                directory = os.getcwd()
                os.makedirs(directory + "/decks/deckstorage/", exist_ok=True)
                target_directory = directory + "/decks/deckstorage/" + username + "/"
                os.makedirs(target_directory, exist_ok=True)
                target_directory = directory + "/decks/deckstorage/" + username + "/" + deck_name
                set_key = False
                if not os.path.exists(target_directory):
                    print("Path does not exist")
                    os.mkdir(target_directory)
                elif force_send == "T":
                    print("Overwriting path")
                    set_key = True
                else:
                    print("path exists")
                    return JsonResponse({'message': 'deck with that name already exists'})
                with open(target_directory + "/content", "w") as file:
                    file.write(text)
                with open(target_directory + "/desc", "w") as file:
                    file.write(description)
                num_tries = 0
                while not set_key:
                    new_key = ''.join(random.choice(
                        string.ascii_uppercase + string.ascii_lowercase + string.digits
                    ) for _ in range(16 + num_tries))
                    print(new_key)
                    if not check_if_key_in_use(new_key):
                        with open(target_directory + "/key", "w") as file:
                            file.write(new_key)
                        set_key = True
                    if num_tries > 100:
                        with open(target_directory + "/key", "w") as file:
                            file.write(new_key)
                        return JsonResponse({'message': 'deck ok'})
                    num_tries += 1
                return JsonResponse({'message': 'deck ok'})
            # message_to_send = "Feedback/" + message_to_send
            message = message_to_send
            return JsonResponse({'message': message})
        if flag == "SETALLY":
            ally_name = request.POST.get('ally_faction')
            warlord_name = request.POST.get('warlord_name')
            warlord = FindCard.find_card(warlord_name, card_array, cards_dict)
            if not ally_name:
                return JsonResponse({'message': 'Ally ok', 'ally_result': 'OK'})
            elif warlord.get_faction() == ally_name:
                return JsonResponse({'message': 'Ally may not match main faction', 'ally_result': 'NO'})
            elif warlord.get_faction() == "Tyranids" or warlord.get_faction() == "Necrons":
                return JsonResponse({'message': 'Main faction does not ally', 'ally_result': 'NO'})
            elif warlord.get_name() == 'Gorzod':
                return JsonResponse({'message': 'Gorzod does not ally', 'ally_result': 'NO'})
            elif warlord.get_name() == "Farseer Tadheris":
                if ally_name == "Space Marines" or ally_name == "Orks":
                    return JsonResponse({'message': 'Ally ok', 'ally_result': 'OK'})
                return JsonResponse({'message': 'Farseer Tadheris allies as if they were Astra Militarum',
                                     'ally_result': 'NO'})
            elif warlord.get_name() == 'Commander Starblaze':
                if ally_name == "Astra Militarum":
                    return JsonResponse({'message': 'Ally ok', 'ally_result': 'OK'})
                else:
                    return JsonResponse({'message': 'Commander Starblaze allies with Astra Militarum only',
                                         'ally_result': 'NO'})
            else:
                ally_ok = False
                position_main_faction = -1
                for i in range(len(alignment_wheel)):
                    if alignment_wheel[i] == warlord.get_faction():
                        position_main_faction = i
                if position_main_faction != -1:
                    ally_pos_1 = (position_main_faction + 1) % 7
                    ally_pos_2 = (position_main_faction - 1) % 7
                    if ally_name == alignment_wheel[ally_pos_1] or ally_name == alignment_wheel[ally_pos_2]:
                        ally_ok = True
                if ally_ok:
                    return JsonResponse({'message': 'Ally ok', 'ally_result': 'OK'})
                return JsonResponse({'message': 'Invalid Ally', 'ally_result': 'NO'})
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
            elif card.get_card_type() == "Token":
                return JsonResponse({'message': 'Cannot add tokens'})
            elif card.get_loyalty() == "Signature":
                return JsonResponse({'message': 'Cannot add Signature units'})
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
                    if card.get_loyalty() == "Common":
                        ally_ok = True
            elif main_faction == "Tyranids":
                if card.get_faction() == "Tyranids" or (card.get_faction() == "Neutral" and card_type != "Army"):
                    ally_ok = True
            elif card.get_faction() == "Neutral":
                ally_ok = True
            elif warlord_name == "Commander Starblaze":
                if ally == "Astra Militarum" and card.get_faction() == "Astra Militarum" and \
                        card.get_loyalty() == "Common":
                    ally_ok = True
            elif warlord_name == "Gorzod":
                if (card.get_faction() == "Space Marines" or card.get_faction() == "Astra Militarum") and \
                        card_type == "Army" and card.get_loyalty() == "Common" and card.check_for_a_trait("Vehicle"):
                    ally_ok = True
            elif warlord_name == "Farseer Tadheris":
                if (card.get_faction() == "Space Marines" or card.get_faction() == "Orks") and \
                            ally == card.get_faction() and card.get_loyalty() == "Common":
                    ally_ok = True
            else:
                position_main_faction = -1
                for i in range(len(alignment_wheel)):
                    if alignment_wheel[i] == warlord.get_faction():
                        position_main_faction = i
                if position_main_faction != -1:
                    ally_pos_1 = (position_main_faction + 1) % 7
                    ally_pos_2 = (position_main_faction - 1) % 7
                    if ally == alignment_wheel[ally_pos_1] or ally == alignment_wheel[ally_pos_2]:
                        if card.get_loyalty() == "Loyal":
                            return JsonResponse({'message': 'Cannot add loyal cards from other factions'})
                        if card.get_loyalty() == "Common":
                            if warlord_name == "Yvraine":
                                if card.get_faction() == "Chaos" and card.check_for_a_trait("Elite"):
                                    return JsonResponse({'message': 'Yvraine cannot have Chaos elites'})
                            ally_ok = True
            if ally_ok:
                if card.check_for_a_trait("Pledge"):
                    card_type = "Pledge"
                return JsonResponse({'message': 'ADDCARD', 'card_type': card_type,
                                     'card_name': card_name})
            else:
                return JsonResponse({'message': 'Card not added'})

    return JsonResponse({'message': 'Invalid request'})
