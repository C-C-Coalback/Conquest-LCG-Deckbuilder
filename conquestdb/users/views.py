from django.shortcuts import render
from django.http import HttpResponseRedirect
import light_dark_dict
import pandas as pd
import os
import datetime
from heapq import nlargest
from card_utils import convert_name_to_img_src, convert_name_to_hyperlink


def get_users_published_decks(username):
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
            if creator == username:
                for file in os.listdir(target_directory + "/" + creator):
                    try:
                        target_file = target_directory + "/" + creator + "/" + file
                        with open(target_file + "/content", "r", encoding="utf-8") as f:
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


def determine_favorite_warlords_public(username):
    distribution = {

    }
    total_decks = 0
    directory = os.getcwd()
    target_directory = directory + "/decks/publisheddecks/"
    if os.path.exists(target_directory):
        for creator in os.listdir(target_directory):
            if creator == username:
                for file in os.listdir(target_directory + "/" + creator):
                    try:
                        target_file = target_directory + "/" + creator + "/" + file
                        with open(target_file + "/content", "r", encoding="utf-8") as f:
                            data = f.read()
                            split_data = data.split(sep="\n")
                            warlord = split_data[2]
                            if warlord not in distribution:
                                distribution[warlord] = 0
                            distribution[warlord] += 1
                            total_decks += 1
                    except Exception as e:
                        print(e)
                        pass
    if total_decks > 0:
        for key in distribution:
            distribution[key] = distribution[key] / total_decks
    return distribution


def determine_favorite_warlords_private(username):
    distribution = {

    }
    total_decks = 0
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/"
    if os.path.exists(target_directory):
        for creator in os.listdir(target_directory):
            if creator == username:
                for file in os.listdir(target_directory + "/" + creator):
                    try:
                        target_file = target_directory + "/" + creator + "/" + file
                        with open(target_file + "/content", "r", encoding="utf-8") as f:
                            data = f.read()
                            split_data = data.split(sep="\n")
                            warlord = split_data[2]
                            if warlord not in distribution:
                                distribution[warlord] = 0
                            distribution[warlord] += 1
                            total_decks += 1
                    except Exception as e:
                        print(e)
                        pass
    if total_decks > 0:
        for key in distribution:
            distribution[key] = distribution[key] / total_decks
    return distribution


def determine_faction_distribution_private(username):
    distribution = {
        "Space Marines": 0,
        "Astra Militarum": 0,
        "Tau": 0,
        "Eldar": 0,
        "Dark Eldar": 0,
        "Chaos": 0,
        "Orks": 0,
        "Tyranids": 0,
        "Necrons": 0
    }
    total_decks = 0
    directory = os.getcwd()
    target_directory = directory + "/decks/deckstorage/"
    if os.path.exists(target_directory):
        for creator in os.listdir(target_directory):
            if creator == username:
                for file in os.listdir(target_directory + "/" + creator):
                    try:
                        target_file = target_directory + "/" + creator + "/" + file
                        with open(target_file + "/content", "r", encoding="utf-8") as f:
                            data = f.read()
                            split_data = data.split(sep="\n")
                            factions = split_data[3]
                            main_faction = factions.split(sep=" (")[0]
                            distribution[main_faction] += 1
                            total_decks += 1
                    except Exception as e:
                        print(e)
                        pass
    if total_decks > 0:
        for key in distribution:
            distribution[key] = distribution[key] / total_decks
    return distribution


def determine_faction_distribution_published(username):
    distribution = {
        "Space Marines": 0,
        "Astra Militarum": 0,
        "Tau": 0,
        "Eldar": 0,
        "Dark Eldar": 0,
        "Chaos": 0,
        "Orks": 0,
        "Tyranids": 0,
        "Necrons": 0
    }
    total_decks = 0
    directory = os.getcwd()
    target_directory = directory + "/decks/publisheddecks/"
    if os.path.exists(target_directory):
        for creator in os.listdir(target_directory):
            if creator == username:
                for file in os.listdir(target_directory + "/" + creator):
                    try:
                        target_file = target_directory + "/" + creator + "/" + file
                        with open(target_file + "/content", "r", encoding="utf-8") as f:
                            data = f.read()
                            split_data = data.split(sep="\n")
                            factions = split_data[3]
                            main_faction = factions.split(sep=" (")[0]
                            distribution[main_faction] += 1
                            total_decks += 1
                    except Exception as e:
                        print(e)
                        pass
    if total_decks > 0:
        for key in distribution:
            distribution[key] = distribution[key] / total_decks
    return distribution


def target_user(request, chosen_user):
    username = request.user.username
    if username == chosen_user:
        return HttpResponseRedirect("/users/")
    deck_names, deck_warlords, deck_dates, img_srcs, keys, creator_name = get_users_published_decks(chosen_user)
    light_dark_toggle = light_dark_dict.get_light_mode(username)
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
        factions_list = []
        faction_percentages = []
        faction_distribution = determine_faction_distribution_published(chosen_user)
        for key in faction_distribution:
            factions_list.append(key)
            faction_percentages.append(str(round(faction_distribution[key] * 100, 1)) + "%")
        sent_factions = zip(factions_list, faction_percentages)
        favorite_warlords = determine_favorite_warlords_public(chosen_user)
        num_entries = len(favorite_warlords)
        warlord_names = []
        try:
            warlord_names = nlargest(min(num_entries, 3), favorite_warlords, key=favorite_warlords.get)
        except Exception as e:
            print(e)
            print("Failed to load favorite warlords.")
        warlord_srcs = []
        warlord_links = []
        for i in range(len(warlord_names)):
            warlord_srcs.append(convert_name_to_img_src(warlord_names[i]))
            warlord_links.append(convert_name_to_hyperlink(warlord_names[i]))
        sent_warlords = zip(warlord_names, warlord_srcs, warlord_links)
        return render(request, "users/target_user.html", {"decks_exist": "Yes", "light_dark_toggle": light_dark_toggle,
                                                          "target_user": chosen_user, "user_exists": "Yes",
                                                          "decks": decks_var, "factions": sent_factions,
                                                          "warlords": sent_warlords})
    except Exception as e:
        print(e)
    return render(request, "users/target_user.html", {"decks_exist": "No", "light_dark_toggle": light_dark_toggle,
                                                      "target_user": chosen_user, "user_exists": "No"})


def own_user(request):
    username = request.user.username
    deck_names, deck_warlords, deck_dates, img_srcs, keys, creator_name = get_users_published_decks(username)
    light_dark_toggle = light_dark_dict.get_light_mode(username)
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
        factions_list = []
        faction_percentages = []
        faction_distribution = determine_faction_distribution_private(username)
        for key in faction_distribution:
            factions_list.append(key)
            faction_percentages.append(str(round(faction_distribution[key] * 100, 1)) + "%")
        sent_factions = zip(factions_list, faction_percentages)
        favorite_warlords = determine_favorite_warlords_private(username)
        num_entries = len(favorite_warlords)
        sent_warlords = []
        warlord_names = []
        try:
            warlord_names = nlargest(min(num_entries, 3), favorite_warlords, key=favorite_warlords.get)
        except Exception as e:
            print(e)
            print("Failed to load favorite warlords.")
        warlord_srcs = []
        warlord_links = []
        for i in range(len(warlord_names)):
            warlord_srcs.append(convert_name_to_img_src(warlord_names[i]))
            warlord_links.append(convert_name_to_hyperlink(warlord_names[i]))
        sent_warlords = zip(warlord_names, warlord_srcs, warlord_links)
        return render(request, "users/own_user.html", {"decks_exist": "Yes", "light_dark_toggle": light_dark_toggle,
                                                       "decks": decks_var, "factions": sent_factions,
                                                       "warlords": sent_warlords})
    except Exception as e:
        print(e)
    return render(request, "users/own_user.html", {"decks_exist": "No", "light_dark_toggle": light_dark_toggle})
