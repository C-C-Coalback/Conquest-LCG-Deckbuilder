from conquestdb.cardscode import Initfunctions


card_array = Initfunctions.init_player_cards()
planet_array = Initfunctions.init_planet_cards()
apoka_errata_array = Initfunctions.init_apoka_errata_cards()

images_dict = {}
cards_dict = {}
planets_dict = {}
apoka_errata_dict = {}
warpacks_list = []
cycles_list = []
traits_list = []
lower_case_dict = {}
lower_case_planet_dict = {}
for i in range(len(card_array)):
    if card_array[i].war_pack not in warpacks_list:
        warpacks_list.append(card_array[i].war_pack)
    if card_array[i].cycle not in cycles_list:
        cycles_list.append(card_array[i].cycle)
    traits = card_array[i].get_traits()
    traits_split = traits.split(sep=". ")
    for trait in traits_split:
        cleaned_trait = trait.replace(".", "")
        if cleaned_trait not in traits_list:
            traits_list.append(cleaned_trait)
traits_list.sort()
for key in range(len(card_array)):
    cards_dict[card_array[key].name] = card_array[key]
    images_dict[card_array[key].image_name] = card_array[key]
    lower_case_dict[card_array[key].name.lower()] = card_array[key]
for key in range(len(planet_array)):
    planets_dict[planet_array[key].name] = planet_array[key]
    images_dict[planet_array[key].image_name] = planet_array[key]
    lower_case_planet_dict[planet_array[key].name.lower()] = planet_array[key]
for key in range(len(apoka_errata_array)):
    apoka_errata_dict[apoka_errata_array[key].image_name] = apoka_errata_array[key]


def get_images_dict():
    return images_dict


def get_cards_dict():
    return cards_dict


def get_planets_dict():
    return planets_dict


def get_apoka_errata_dict():
    return apoka_errata_dict


def get_warpacks_list():
    return warpacks_list


def get_cycles_list():
    return cycles_list


def get_traits_list():
    return traits_list


def get_lower_case_dict():
    return lower_case_dict


def get_lower_case_planet_dict():
    return lower_case_planet_dict
