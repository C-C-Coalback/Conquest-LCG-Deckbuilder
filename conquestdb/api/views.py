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
                deck_content = deck_content.replace(
                    "Army", "")
                deck_content = deck_content.replace(
                    "Support", "")
                deck_content = deck_content.replace(
                    "Event", "")
                deck_content = deck_content.replace(
                    "Attachment", "")
                deck_content = deck_content.replace(
                    "Synapse", "")
                deck_content = deck_content.replace(
                    "Pledge", "")
                deck_content = deck_content.replace(
                    "Planet", "")
                deck_content = deck_content.replace(
                    "Signature Squad", "")
                deck_content = deck_content.split(sep="\n")
                deck_content = [x for x in deck_content if x != ""]
                del deck_content[0]
                del deck_content[1]
                # deck_content = "\n".join(deck_content)
                return JsonResponse({'message': 'DECK FOUND', 'deck_content': deck_content})
        except Exception as e:
            print(e)
        return JsonResponse({'message': 'DECK NOT FOUND', 'deck_content': ""})
    return render(request, "home.html")


def tts_welcome(request):
    if request.method == 'GET':
        print("received get request")
        return JsonResponse({'message': 'You have reached the deckbuilder!'})
    return render(request, "home.html")
