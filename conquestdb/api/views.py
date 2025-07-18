from django.shortcuts import render
from django.http import JsonResponse
from conquestdb.cardscode import Initfunctions
from conquestdb.cardscode import FindCard
from django.http import HttpResponseRedirect
import os
import copy
import datetime
import random
import string
import shutil
import json

dire = os.getcwd()
dire = dire + "/api/imagelinkslookup/all/"
with open(dire + "front.json") as json_file:
    front_links = json.load(json_file)
with open(dire + "back.json") as json_file:
    back_links = json.load(json_file)
with open(dire + "desc.json") as json_file:
    desc_links = json.load(json_file)
with open(dire + "card_id.json") as json_file:
    card_id_links = json.load(json_file)
with open(dire + "deck_id.json") as json_file:
    deck_id_links = json.load(json_file)
with open(dire + "height.json") as json_file:
    height_links = json.load(json_file)
with open(dire + "width.json") as json_file:
    width_links = json.load(json_file)
with open(dire + "unique.json") as json_file:
    unique_links = json.load(json_file)
with open(dire + "hidden.json") as json_file:
    hidden_links = json.load(json_file)


generic_back = "https://steamusercontent-a.akamaihd.net/ugc/1656728123510442187/" \
               "0B3B69362D3729BC3AEDEBE665D6DF9A9E0AB627/"


def get_hidden_link(name_card):
    if name_card in hidden_links:
        return hidden_links[name_card]
    return False


def get_unique_link(name_card):
    if name_card in unique_links:
        return unique_links[name_card]
    return False


def get_front_link(name_card):
    if name_card in front_links:
        return front_links[name_card]
    return generic_back


def get_back_link(name_card):
    if name_card in back_links:
        return back_links[name_card]
    return generic_back


def get_desc(name_card):
    if name_card in desc_links:
        return desc_links[name_card]
    return ""


def get_card_id(name_card):
    if name_card in card_id_links:
        return card_id_links[name_card]
    return -1


def get_deck_id(name_card):
    if name_card in deck_id_links:
        return deck_id_links[name_card]
    return -1


def get_height(name_card):
    if name_card in height_links:
        return height_links[name_card]
    return 1


def get_width(name_card):
    if name_card in width_links:
        return width_links[name_card]
    return 1


def send_deck_given_key(key_string):
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
                            with open(second_target_directory + "/" + deck_name + "/content", "r") as d:
                                return d.read()
    target_directory = directory + "/decks/publisheddecks/"
    for username in os.listdir(target_directory):
        if username:
            second_target_directory = target_directory + "/" + username
            for deck_name in os.listdir(second_target_directory):
                if os.path.exists(second_target_directory + "/" + deck_name + "/key"):
                    with open(second_target_directory + "/" + deck_name + "/key", "r") as f:
                        this_key = f.read()
                        if this_key == key_string:
                            with open(second_target_directory + "/" + deck_name + "/content", "r") as d:
                                return d.read()
    return ""


def nothing(request):
    return render(request, "home.html")


def request_deck(request, deck_key):
    if request.method == 'GET':
        print("received get request, deck key:", deck_key)
        try:
            deck_content = send_deck_given_key(deck_key)
            if deck_content:
                deck_content = deck_content.replace(
                    "----------------------------------------------------------------------", "")
                deck_content = deck_content.split(sep="\n")
                if "Planet" in deck_content:
                    deck_content.remove("Planet")
                if "Signature Squad" in deck_content:
                    deck_content.remove("Signature Squad")
                if "Pledge" in deck_content:
                    deck_content.remove("Pledge")
                if "Synapse" in deck_content:
                    deck_content.remove("Synapse")
                if "Attachment" in deck_content:
                    deck_content.remove("Attachment")
                if "Event" in deck_content:
                    deck_content.remove("Event")
                if "Army" in deck_content:
                    deck_content.remove("Army")
                if "Support" in deck_content:
                    deck_content.remove("Support")
                deck_content = [x for x in deck_content if x != ""]
                card_amounts = []
                del deck_content[0]
                del deck_content[1]
                for i in range(len(deck_content)):
                    if i == 0:
                        card_amounts.append(1)
                    else:
                        card_amounts.append(int(deck_content[i][0]))
                front_links_sent = []
                back_links_sent = []
                desc_links_sent = []
                card_id_links_sent = []
                deck_id_links_sent = []
                height_links_sent = []
                width_links_sent = []
                nicknames_sent = []
                hidden_links_sent = []
                unique_links_sent = []
                for i in range(len(deck_content)):
                    if i == 0:
                        print(deck_content[i])
                        front_links_sent.append(get_front_link(deck_content[i]))
                        back_links_sent.append(get_back_link(deck_content[i]))
                        desc_links_sent.append(get_desc(deck_content[i]))
                        card_id_links_sent.append(get_card_id(deck_content[i]))
                        deck_id_links_sent.append(get_deck_id(deck_content[i]))
                        height_links_sent.append(get_height(deck_content[i]))
                        width_links_sent.append(get_width(deck_content[i]))
                        nicknames_sent.append(deck_content[i])
                        hidden_links_sent.append(get_hidden_link(deck_content[i]))
                        unique_links_sent.append((get_unique_link(deck_content[i])))
                    else:
                        print(deck_content[i][3:])
                        nicknames_sent.append(deck_content[i][3:])
                        front_links_sent.append(get_front_link(deck_content[i][3:]))
                        back_links_sent.append(get_back_link(deck_content[i][3:]))
                        desc_links_sent.append("")
                        card_id_links_sent.append(get_card_id(deck_content[i][3:]))
                        deck_id_links_sent.append(get_deck_id(deck_content[i][3:]))
                        height_links_sent.append(get_height(deck_content[i][3:]))
                        width_links_sent.append(get_width(deck_content[i][3:]))
                        hidden_links_sent.append(get_hidden_link(deck_content[i][3:]))
                        unique_links_sent.append((get_unique_link(deck_content[i][3:])))
                return JsonResponse({'message': 'DECK FOUND', 'deck_content': nicknames_sent,
                                     'front': front_links_sent, 'back': back_links_sent,
                                     'card_id': card_id_links_sent, 'deck_id': deck_id_links_sent,
                                     'height': height_links_sent, 'width': width_links_sent,
                                     'amount': card_amounts, 'desc': desc_links_sent,
                                     'hidden': hidden_links_sent, 'unique': unique_links_sent})
        except Exception as e:
            print(e)
        return JsonResponse({'message': 'DECK NOT FOUND', 'deck_content': ""})
    return render(request, "home.html")


def tts_welcome(request):
    if request.method == 'GET':
        print("received get request")
        return JsonResponse({'message': 'You have reached the deckbuilder!'})
    return render(request, "home.html")
