from django.shortcuts import render
from conquestdb.cardscode import Initfunctions
import pandas as pd
from django.http import JsonResponse


card_array = Initfunctions.init_player_cards()
planet_array = Initfunctions.init_planet_cards()
apoka_errata_array = Initfunctions.init_apoka_errata_cards()


df = pd.DataFrame([x.as_dict() for x in card_array])


def index(request):
    return render(request, 'cards/index.html')

# View to handle the Ajax request
def ajax_view(request):
    if request.method == 'POST':
        card_names = []
        search = request.POST.get('search')
        faction = request.POST.get('faction')
        print(faction)
        filtered_df = df
        if search is not None:
            filtered_df = filtered_df[filtered_df['name'].str.contains(search)]
        if faction is not None:
            filtered_df = filtered_df.loc[filtered_df['faction'] == faction]
        card_names = filtered_df['name'].to_list()
        image_names = filtered_df['image name'].to_list()
        card_names = card_names[:4]
        image_names = image_names[:4]
        message = f'Faction, {faction}'
        print(image_names)
        return JsonResponse({'message': message, 'cards': card_names, 'image_names': image_names})
    return JsonResponse({'message': 'Invalid request'})


def card_data(request, card_name):
    return render(request, "cards/card_data.html", {"card_name": card_name})
