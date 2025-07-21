from django.shortcuts import render
from django.http import JsonResponse
from conquestdb.cardscode import Initfunctions
from conquestdb.cardscode import FindCard
from django.http import HttpResponseRedirect
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
        for i in range(len(alignment_wheel)):
            if alignment_wheel[i] == factions[0]:
                position_main_faction = i
        if position_main_faction != -1:
            ally_pos_1 = (position_main_faction + 1) % 7
            ally_pos_2 = (position_main_faction - 1) % 7
            if factions[1] == alignment_wheel[ally_pos_1] \
                    or factions[1] == alignment_wheel[ally_pos_2]:
                return deck_validation(deck, remaining_signature_squad, factions)
            elif factions[1] == "Astra Militarum" and warlord_card.get_name() == "Commander Starblaze":
                return deck_validation(deck, remaining_signature_squad, factions, "Commander Starblaze")
        return "Issue with faction matching."
    return "Unknown issue"


def deck_validation(deck, remaining_signature_squad, factions, warlord=""):
    global card_array
    global cards_dict
    print("Can continue")
    current_index = 4
    if deck[current_index] == "Signature Squad":
        card = FindCard.find_card(deck[current_index - 1], card_array, cards_dict)
        print(deck[current_index - 1])
        if card.check_for_a_trait("Pledge"):
            current_index = 5
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
                else:
                    return "Synapse units not allowed in this deck"
            faction_check_passed = False
            if card_result.get_faction() == factions[0]:
                faction_check_passed = True
            elif card_result.get_faction() == factions[1] and card_result.get_loyalty() == "Common":
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
                return "Faction check not passed (Main, Ally, Card): "\
                       + factions[0] + factions[1] + card_result.get_faction()
        current_index += 1
        while deck[current_index] in skippers:
            current_index += 1
    if synapse_needed and not has_synapse:
        return "No Synapse Unit Given"
    if card_count < 42:
        print("Too few cards")
        print(card_count)
        return "Too few cards: " + str(card_count)
    print("No issues")
    return "SUCCESS"


def decks(request):
    deck_names, deck_warlords, deck_dates, img_srcs, keys, creator_name = get_published_decks_lists()
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

        return render(request, "decks/home_decks.html", {"decks_exist": "Yes", "decks": decks_var})
    except Exception as e:
        print(e)
    return render(request, "decks/home_decks.html", {"decks_exist": "No"})


def delete_deck(request, deck_key):
    print("delete deck")
    delete_private_deck(deck_key, request.user.username)
    return HttpResponseRedirect('/decks/my_decks/')


def retract_deck(request, deck_key):
    print("delete deck")
    delete_published_deck(deck_key, request.user.username)
    return HttpResponseRedirect('/decks/my_decks/')


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
                        timestamp = os.path.getmtime(target_file + "/content")
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


def published_decks(request):
    deck_names, deck_warlords, deck_dates, img_srcs, keys, creator_name = get_published_decks_lists()
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
        return render(request, "decks/published_decks.html", {"decks": decks_var})
    except Exception as e:
        print(e)
    decks_var = zip(deck_names, deck_warlords, deck_dates, img_srcs, keys, creator_name)
    return render(request, "decks/published_decks.html", {"decks": decks_var})


def my_decks(request):
    deck_names = []
    deck_warlords = []
    deck_dates = []
    img_srcs = []
    keys = []
    username = request.user.username
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/" + username + "/"
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
                        timestamp = os.path.getmtime(target_file + "/content")
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
        return render(request, "decks/mydecks.html", {"decks": decks_var})
    except Exception as e:
        print(e)
    decks_var = zip(deck_names, deck_warlords, deck_dates, img_srcs, keys)
    return render(request, "decks/mydecks.html", {"decks": decks_var})


def modify_deck(request, deck_key):
    username = request.user.username
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/" + username + "/"
    data = []
    desc = ""
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
                                                         "auto_complete": card_names_array})
    return render(request, "decks/createdeck.html", {"edit": "F", "data": "", "desc": "",
                                                     "auto_complete": card_names_array})


def create_deck(request):
    return render(request, "decks/createdeck.html", {"edit": "F", "data": "", "desc": "",
                                                     "auto_complete": card_names_array})


def user_deck_data(request, deck_creator):
    return render(request, "decks/user_deck_data.html")


def deck_data(request, deck_creator, deck_key):
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
        synapse_name = ""
        pledge_name = ""
        for i in range(len(deck_list)):
            if deck_list[i] == "Signature Squad":
                sig_pos = i
                if deck_list[i - 1] in pledges_array:
                    pledge_name = deck_list[i - 1]
            if deck_list[i] == "Army":
                army_pos = i
            if deck_list[i] == "Support":
                support_pos = i
            if deck_list[i] == "Event":
                event_pos = i
            if deck_list[i] == "Attachment":
                attachment_pos = i
            if deck_list[i] == "Synapse":
                if deck_list[i + 1] != "Attachment":
                    synapse_name = deck_list[i + 1]
                synapse_pos = i
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
                        times_comments.append(split_text[1])
                        comments.append(split_text[2])
                        no_comments = False
        my_comments = zip(names_comments, times_comments, comments, comment_ids)
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
                                                        "pledge_img": pledge_img, "pledge_link": pledge_link})
    return render(request, "decks/deck_data.html", {"deck_found": deck_found})


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


def ajax_view(request):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        if flag == "SENDDECK":
            text = request.POST.get('deck_text')
            username = request.POST.get('username')
            description = request.POST.get('description')
            force_send = request.POST.get('force_send')
            message_to_send = ""
            text = text.replace("\"Subject: &Omega;-X62113\"", "")
            text = text.replace("idden Base", "'idden Base")
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
                    if card.get_loyalty() == "Common":
                        ally_ok = True
            elif main_faction == "Tyranids":
                if card.get_faction() == "Tyranids" or (card.get_faction() == "Neutral" and card_type != "Army"):
                    ally_ok = True
            elif card.get_faction() == "Neutral":
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
                            ally_ok = True
            if ally_ok:
                if card.check_for_a_trait("Pledge"):
                    card_type = "Pledge"
                return JsonResponse({'message': 'ADDCARD', 'card_type': card_type,
                                     'card_name': card_name})
            else:
                return JsonResponse({'message': 'Card not added'})

    return JsonResponse({'message': 'Invalid request'})
