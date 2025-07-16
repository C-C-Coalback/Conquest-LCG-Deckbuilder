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


def nothing(request):
    return render(request, "home.html")


def request_deck(request, deck_key):
    if request.method == 'POST':
        print("received post request, deck key:", deck_key)
    return render(request, "home.html")


def tts_welcome(request):
    if request.method == 'POST':
        print("received post request")
    return render(request, "home.html")
