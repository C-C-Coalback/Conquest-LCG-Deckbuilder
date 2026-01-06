from django.shortcuts import render, redirect
from conquestdb.cardscode import Initfunctions
import pandas as pd
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from conquestdb.cardscode import FindCard
import ast
import os
import os.path
import datetime
import light_dark_dict
from card_utils import convert_name_to_img_src, convert_name_to_hyperlink, convert_name_to_create_deck_hyperlink
from PIL import Image, ImageDraw, ImageFont
from .custom_card_creator.dict_inits.card_types_dict_positions import card_types_dictionary_positions
from .custom_card_creator.dict_inits.command_dict import command_dictionary
from .custom_card_creator.dict_inits.loyalty_dict import loyalty_dictionary
from .custom_card_creator.dict_inits.icons_dict import icons_dict, special_text_dict
import random
import string
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile


def sorter_cycles(column):
    order_of_cycles = ['Core Set', 'Warlord Cycle', 'The Great Devourer', 'Planetfall Cycle',
                       'Legions of Death', 'Death World Cycle', 'Navida Prime Cycle',
                       'Defenders of the Faith', 'Confrontation Cycle',
                       'Chronicles of Heroes', 'Bloodied Path Cycle']
    cat = pd.Categorical(column, categories=order_of_cycles, ordered=True)
    return pd.Series(cat)


def sorter_warpacks(column):
    order_of_warpacks = ['Core Set',
                         'The Howl of Blackmane', 'The Scourge', 'Gift of the Ethereals',
                         "Zogwort's Curse", 'The Threat Beyond', 'Descendants of Isha',
                         'The Great Devourer',
                         'Decree of Ruin', 'Boundless Hate', 'Deadly Salvage',
                         'What Lurks Below', 'Wrath of the Crusaders', 'The Final Gambit',
                         'Legions of Death',
                         'Jungles of Nectavus', 'Unforgiven', 'Slash and Burn',
                         'Searching for Truth', 'Against the Great Enemy', 'The Warp Unleashed',
                         'Enemy Territory', 'Promise of War', 'Aligned Stars',
                         'Overrun', 'Breaching the Veil',
                         'Defenders of the Faith',
                         'By Imperial Decree', 'A Mask Falls Off', 'The Laughing God',
                         'Chronicles of Heroes',
                         'The Shadow in the Warp', 'Herald of the Plague God', 'For the Enclaves']
    cat = pd.Categorical(column, categories=order_of_warpacks, ordered=True)
    return pd.Series(cat)


card_array = Initfunctions.init_player_cards()
planet_array = Initfunctions.init_planet_cards()
apoka_errata_array = Initfunctions.init_apoka_errata_cards()
images_dict = {}
cards_dict = {}
planets_dict = {}
apoka_errata_dict = {}
banned_cards = ["Bonesinger Choir", "Squiggoth Brute", "Corrupted Teleportarium", "Gun Drones", "Archon's Palace",
                "Land Speeder Vengeance", "Sowing Chaos", "Smasha Gun Battery", "The Prince's Might",
                "Purveyor of Hubris", "Doom", "Exterminatus", "Mind Shackle Scarab",
                "Crypt of Saint Camila", "Warpstorm"]
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

df = pd.DataFrame([x.as_dict() for x in card_array])
planet_df = pd.DataFrame([x.as_dict() for x in planet_array])


def index(request):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    return render(request, 'cards/index.html', {
        "light_dark_toggle": light_dark_toggle, "cycles_list": cycles_list, "warpacks_list": warpacks_list,
        "traits_list": traits_list
    })


card_types = ["Warlord", "Army", "Support", "Event", "Attachment", "Synapse", "Planet"]
factions = ["Space Marines", "Astra Militarum", "Orks", "Chaos", "Dark Eldar",
            "Eldar", "Tau", "Necrons", "Tyranids", "Neutral"]
loyalties = ["Common", "Loyal", "Signature"]
shields = ["0", "1", "2", "3"]


# (1440, 2052) card size


def get_pil_text_size(text, font_size, font_name):
    font = ImageFont.truetype(font_name, font_size)
    size = font.getbbox(text)
    return size


def get_position_text(card_type, faction, text_type):
    return card_types_dictionary_positions[card_type][faction][text_type]


def get_resize_command(faction, command_type):
    return command_dictionary[faction]["Resize"][command_type]


def get_position_command(faction, command_type):
    return command_dictionary[faction][command_type]


def get_position_loyalty(faction, card_type):
    return loyalty_dictionary[card_type][faction]


def get_true_string_for_fonts(text):
    for icon in icons_dict:
        if icon in text:
            text = text.replace(icon, icons_dict[icon]["spacing"])
    return text


def get_wrapped_text(text: str, font: ImageFont.ImageFont, line_length: int):
    lines = ['']
    actual_lines = ['']
    for word in text.split():
        before_replace = word.strip()
        replaced_word = get_true_string_for_fonts(before_replace)
        line = f'{lines[-1]} {replaced_word}'
        actual_line = f'{actual_lines[-1]} {word}'.strip()
        if font.getlength(line) <= line_length:
            lines[-1] = line
            actual_lines[-1] = actual_line
        else:
            lines.append(replaced_word)
            actual_lines.append(word)
    return '\n'.join(actual_lines)


def get_wrapped_text_nlfix(text: str, font: ImageFont.ImageFont, line_length: int):
    return "\n".join([get_wrapped_text(line, font, line_length) for line in text.splitlines()])


def clicked():
    pass


def add_text_to_image(input_image, text, coords,
                      font_src="cards/custom_card_creator/fonts/Markazi_Text/MarkaziText-VariableFont_wght.ttf",
                      font_size=84, color=(0, 0, 0), line_length=1080,
                      font_bold="cards/custom_card_creator/fonts/Markazi_Text/static/MarkaziText-Bold.ttf",
                      font_italics="cards/custom_card_creator/fonts/open_sans/OpenSans-Italic.ttf", deepstrike=False):
    text = text.replace("[DARK ELDAR]", "[DARK_ELDAR]")
    text = text.replace("[SPACE MARINES]", "[SPACE_MARINES]")
    text = text.replace("[ASTRA MILITARUM]", "[ASTRA_MILITARUM]")
    text = text.replace("[DEPLOY ACTION]", "[DEPLOY_ACTION]")
    text = text.replace("[COMMAND ACTION]", "[COMMAND_ACTION]")
    text = text.replace("[COMBAT ACTION]", "[COMBAT_ACTION]")
    text = text.replace("[HEADQUARTERS ACTION]", "[HEADQUARTERS_ACTION]")
    text = text.replace("[GOES FASTA]", "[GOES_FASTA]")
    text = text.replace("[HIVE MIND]", "[HIVE_MIND]")
    if deepstrike:
        color = (255, 0, 0)
    drawn_image = ImageDraw.Draw(input_image)
    text_font = ImageFont.truetype(font_src, font_size)
    text = get_wrapped_text_nlfix(text, text_font, line_length)
    og_split_text = text.split(sep="\n")
    for item in special_text_dict:
        for i in range(len(og_split_text)):
            while item in og_split_text[i]:
                current_x_pos_text = og_split_text[i].find(item)
                shortened_text = og_split_text[i][:current_x_pos_text]
                for any_icon in icons_dict:
                    shortened_text = shortened_text.replace(any_icon, icons_dict[any_icon]["spacing"])
                for any_icon in special_text_dict:
                    shortened_text = shortened_text.replace(any_icon, special_text_dict[any_icon]["spacing"])
                x_offset = int(text_font.getlength(shortened_text))
                x_pos_icon = coords[0] + x_offset + special_text_dict[item]["initial_extra_offset"][0]
                y_pos_icon = coords[1] + special_text_dict[item]["initial_extra_offset"][1] + (font_size - 8) * i
                if special_text_dict[item]["type"] == "Bold":
                    f_bold = ImageFont.truetype(font_bold, font_size)
                    txt_bold = Image.new('RGBA', (line_length, 330))
                    d_bold = ImageDraw.Draw(txt_bold)
                    d_bold.text((0, 0), special_text_dict[item]["text"], font=f_bold, fill="black")
                    input_image.paste(txt_bold, (x_pos_icon, y_pos_icon), txt_bold)
                else:
                    f_italics = ImageFont.truetype(font_italics, font_size * 0.75)
                    txt_italics = Image.new('RGBA', (line_length, 330))
                    d_bold = ImageDraw.Draw(txt_italics)
                    d_bold.text((0, 0), special_text_dict[item]["text"], font=f_italics, fill="black")
                    input_image.paste(txt_italics, (x_pos_icon, y_pos_icon), txt_italics)
                og_split_text[i] = og_split_text[i].replace(item, special_text_dict[item]["spacing"], 1)
        text = text.replace(item, special_text_dict[item]["spacing"])
    og_split_text = text.split(sep="\n")
    for icon in icons_dict:
        for i in range(len(og_split_text)):
            while icon in og_split_text[i]:
                current_x_pos_text = og_split_text[i].find(icon)
                shortened_text = og_split_text[i][:current_x_pos_text]
                for any_icon in icons_dict:
                    shortened_text = shortened_text.replace(any_icon, icons_dict[any_icon]["spacing"])
                for any_icon in special_text_dict:
                    shortened_text = shortened_text.replace(any_icon, special_text_dict[any_icon]["spacing"])
                x_offset = int(text_font.getlength(shortened_text))
                initial_extra_offset = icons_dict[icon]["initial_extra_offset"]
                extra_vertical_offset = icons_dict[icon]["extra_vertical_line_offset"]
                x_pos_icon = coords[0] + x_offset + initial_extra_offset[0]
                y_pos_icon = coords[1] + initial_extra_offset[1] + (font_size + extra_vertical_offset) * i
                required_size = icons_dict[icon]["resize"]
                text_icon_img = Image.open(icons_dict[icon]["src"], 'r').convert("RGBA")
                text_icon_img = text_icon_img.resize(required_size)
                input_image.paste(text_icon_img, (x_pos_icon, y_pos_icon), text_icon_img)
                og_split_text[i] = og_split_text[i].replace(icon, icons_dict[icon]["spacing"], 1)
        text = text.replace(icon, icons_dict[icon]["spacing"])
    split_text = text.split(sep="\n")
    current_coords = coords
    for i in range(len(split_text)):
        drawn_image.text(current_coords, split_text[i], fill=color, font=text_font)
        current_coords = (current_coords[0], current_coords[1] + (font_size - 8))
    return input_image


def add_text_to_planet_image(input_image, text,
                             font_src="cards/custom_card_creator/fonts/Markazi_Text/MarkaziText-VariableFont_wght.ttf",
                             font_size=84, line_length=1080,
                             font_bold="cards/custom_card_creator/fonts/Markazi_Text/static/MarkaziText-Bold.ttf"):
    text_font = ImageFont.truetype(font_src, font_size)
    text = get_wrapped_text_nlfix(text, text_font, line_length)
    og_split_text = text.split(sep="\n")
    replacement_icons = ["[SPACE MARINES]", "[ASTRA MILITARUM]", "[ORKS]", "[CHAOS]", "[DARK ELDAR]",
                         "[ELDAR]", "[TAU]", "[TYRANIDS]", "[NECRONS]", "[RESOURCE]",
                         "[TECHNOLOGY]", "[MATERIAL]", "[STRONGPOINT]"]
    coords = (30, 400)
    for icon in replacement_icons:
        for i in range(len(og_split_text)):
            if icon in og_split_text[i]:
                current_x_pos_text = og_split_text[i].find(icon)
                shortened_text = og_split_text[i][:current_x_pos_text]
                x_offset = int(text_font.getlength(shortened_text))
                initial_extra_offset = icons_dict[icon]["initial_extra_offset"]
                extra_vertical_offset = icons_dict[icon]["extra_vertical_line_offset"]
                x_pos_icon = coords[0] + 240 + initial_extra_offset[0] - (font_size + extra_vertical_offset) * i
                y_pos_icon = coords[1] + x_offset + initial_extra_offset[1]
                required_size = icons_dict[icon]["resize"]
                text_icon_img = Image.open(icons_dict[icon]["src"], 'r').convert("RGBA")
                text_icon_img = text_icon_img.resize(required_size)
                text_icon_img = text_icon_img.rotate(270)
                input_image.paste(text_icon_img, (x_pos_icon, y_pos_icon), text_icon_img)
                "A Non-[TAU] Unit."
        text = text.replace(icon, icons_dict[icon]["spacing"])
    for item in special_text_dict:
        for i in range(len(og_split_text)):
            if item in og_split_text[i]:
                current_x_pos_text = og_split_text[i].find(item)
                shortened_text = og_split_text[i][:current_x_pos_text]
                x_offset = int(text_font.getlength(shortened_text))
                x_offset = x_offset + special_text_dict[item]["initial_extra_offset"][0] + 400
                y_offset = special_text_dict[item]["initial_extra_offset"][1] - (font_size + 0) * i + 30
                f_bold = ImageFont.truetype(font_bold, font_size)
                txt_bold = Image.new('RGBA', (line_length, 330))
                d_bold = ImageDraw.Draw(txt_bold)
                d_bold.text((0, 0), special_text_dict[item]["text"], font=f_bold, fill="black")
                w_bold = txt_bold.rotate(270, expand=1)
                input_image.paste(w_bold, (y_offset, x_offset), w_bold)
        text = text.replace(item, special_text_dict[item]["spacing"])
    f = ImageFont.truetype(font_src, font_size)
    txt = Image.new('RGBA', (line_length, 330))
    d = ImageDraw.Draw(txt)
    d.text((0, 0), text, font=f, fill="black")
    w = txt.rotate(270, expand=1)
    x_offset = 400
    input_image.paste(w, (30, x_offset), w)
    return input_image


def add_name_to_card(card_type, name, resulting_img):
    if card_type == "Support":
        f = ImageFont.truetype("cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf", 84)
        txt = Image.new('RGBA', (900, 100))
        d = ImageDraw.Draw(txt)
        d.text((0, 0), name, font=f, fill="black")
        w = txt.rotate(90, expand=1)
        x_offset = int((0.5 * get_pil_text_size(name, 84,
                                                "cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf")[
            2]) - 100)
        resulting_img.paste(w, (110, x_offset), w)
    elif card_type == "Planet":
        f = ImageFont.truetype("cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf", 84)
        txt = Image.new('RGBA', (900, 100))
        d = ImageDraw.Draw(txt)
        d.text((0, 0), name, font=f, fill="black")
        w = txt.rotate(270, expand=1)
        x_offset = int((-1 * get_pil_text_size(name, 84,
                                               "cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf")[
            2]))
        x_offset = x_offset + 1900
        resulting_img.paste(w, (1210, x_offset), w)
    elif card_type == "Attachment":
        x_offset = int(690 - (0.5 * get_pil_text_size(name, 84,
                                                      "cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf")[
            2]))
        add_text_to_image(
            resulting_img, name, (x_offset, 1220),
            font_src="cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf"
        )
    elif card_type == "Warlord":
        x_offset = int(750 - (0.5 * get_pil_text_size(name, 84,
                                                      "cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf")[
            2]))
        add_text_to_image(
            resulting_img, name, (x_offset, 94),
            font_src="cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf"
        )
    elif card_type == "Event":
        x_offset = int(810 - (0.5 * get_pil_text_size(name, 84,
                                                      "cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf")[
            2]))
        add_text_to_image(
            resulting_img, name, (x_offset, 78),
            font_src="cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf"
        )
    else:
        x_offset = int(810 - (0.5 * get_pil_text_size(name, 84,
                                                      "cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf")[
            2]))
        add_text_to_image(
            resulting_img, name, (x_offset, 108),
            font_src="cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf"
        )
    return resulting_img


def add_traits_to_card(card_type, traits, resulting_img):
    x_offset = int(840 - (0.5 * get_pil_text_size(traits, 84,
                                                  "cards/custom_card_creator/fonts/Markazi_Text/static/MarkaziText-Bold.ttf")[
        2]))
    y_offset = 1320
    if card_type == "Army":
        x_offset = x_offset - 50
    if card_type == "Support":
        x_offset = x_offset - 100
        y_offset = 1370
    if card_type == "Warlord":
        x_offset = x_offset - 80
        y_offset = 230
    if card_type == "Attachment":
        x_offset = x_offset - 140
        y_offset = 1370
    if card_type == "Event":
        x_offset = x_offset - 100
        y_offset = 1390
    add_text_to_image(
        resulting_img, traits, (x_offset, y_offset),
        font_src="cards/custom_card_creator/fonts/andada/AndadaSC-BoldItalic.otf",
        font_size=60
    )
    return resulting_img


def add_command_icons(command, first_command_src, extra_command_src,
                      command_end_src, resulting_img, faction, card_type):
    command = int(command)
    if command > 0:
        if faction != "Tyranids":
            current_x_pos_end_command, y_end_command = get_position_command(faction, "End")
            first_command_img = Image.open(first_command_src, 'r').convert("RGBA")
            first_command_img = first_command_img.resize(get_resize_command(faction, "First"))
            resulting_img.paste(first_command_img, get_position_command(faction, "First"), first_command_img)
            extra_command_img = Image.open(extra_command_src, 'r').convert("RGBA")
            extra_command_img = extra_command_img.resize(get_resize_command(faction, "Extra"))
            current_position_command, y_extra_command = get_position_command(faction, "Extra")
            spacing = get_position_command(faction, "Spacing")
            for i in range(command - 1):
                resulting_img.paste(extra_command_img, (current_position_command, y_extra_command), extra_command_img)
                current_position_command += spacing
                current_x_pos_end_command += spacing
            command_end_img = Image.open(command_end_src, 'r').convert("RGBA")
            command_end_img = command_end_img.resize(get_resize_command(faction, "End"))
            resulting_img.paste(command_end_img, (current_x_pos_end_command, y_end_command), command_end_img)
        elif (0 < command < 4 and card_type == "Army") or (0 < command < 3 and card_type == "Synapse"):
            str_command = str(command)
            first_command_src = "cards/custom_card_creator/card_srcs/" + faction + \
                                "/" + card_type + "/" + str(command) + "_Command.png"
            first_command_img = Image.open(first_command_src, 'r').convert("RGBA")
            first_command_img = first_command_img.resize(get_resize_command(faction, str_command))
            resulting_img.paste(first_command_img, get_position_command(faction, "First"), first_command_img)


def card_creator(request):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    current_src = "/static/images/CardImages/Nazdreg.jpg"
    username = request.user.username
    if username:
        cwd = os.getcwd()
        if os.path.exists(cwd + "/media/card_img_srcs/" + username):
            file_names = os.listdir(cwd + "/media/card_img_srcs/" + username)
            if file_names:
                current_src = "/media/card_img_srcs/" + username + "/" + file_names[0]
    return render(request, 'cards/card_creator.html', {
        "light_dark_toggle": light_dark_toggle, "current_src": current_src
    })


def process_submitted_planet_card(name, card_type, text, cards_value, resources_value, icons_grouped, output_dir,
                                  input_src):
    resources_src = "cards/custom_card_creator/card_srcs/Planet/Values/resource_" + resources_value + ".jpg"
    cards_src = "cards/custom_card_creator/card_srcs/Planet/Values/card_" + cards_value + ".jpg"
    text_src = "cards/custom_card_creator/card_srcs/" + card_type + "/Text/Text.png"
    if not os.path.exists(text_src):
        return False
    card_art_src = input_src
    expansion_icon_src = "cards/custom_card_creator/current_card_info/expansion_icon/expansion_icon.png"
    resulting_img = Image.new("RGBA", (1440, 2052))
    dirs_art = os.listdir(card_art_src)
    if not dirs_art:
        return False
    random.shuffle(dirs_art)
    card_art_img = Image.open(card_art_src + dirs_art[0], 'r').convert("RGBA")
    card_art_img = card_art_img.resize((1440, 2052))
    resulting_img.paste(card_art_img, get_position_text(card_type, "Planet", "Art"))
    text_resize_amount = (1440, 2052)
    text_img = Image.open(text_src, 'r').convert("RGBA")
    text_img = text_img.resize(text_resize_amount)
    resulting_img.paste(text_img, get_position_text(card_type, "Planet", "Text Box"), text_img)
    if os.path.exists(cards_src):
        cards_value_img = Image.open(cards_src, 'r').convert("RGBA")
        cards_value_img = cards_value_img.resize((256, 176))
        resulting_img.paste(cards_value_img, get_position_text(card_type, "Planet", "Card"), cards_value_img)
    if os.path.exists(resources_src):
        resources_value_img = Image.open(resources_src, 'r').convert("RGBA")
        resources_value_img = resources_value_img.resize((202, 142))
        resulting_img.paste(resources_value_img, get_position_text(card_type, "Planet", "Resource"),
                            resources_value_img)
    expansion_icon_img = Image.open(expansion_icon_src, 'r').convert("RGBA").resize((40, 40))
    resulting_img.paste(expansion_icon_img, get_position_text(card_type, "Planet", "Expansion Icon"),
                        expansion_icon_img)
    add_name_to_card(card_type, name, resulting_img)
    x_offset = int(690 - (0.5 * get_pil_text_size(
        text, 84, "cards/custom_card_creator/fonts/billboard-college-cufonfonts/Billboard-College.ttf"
    )[2]))
    add_text_to_planet_image(
        resulting_img, text
    )
    num_icons = 0
    for c in icons_grouped:
        if c == "R":
            material_src = "cards/custom_card_creator/card_srcs/Planet/Icons/Material.png"
            material_img = Image.open(material_src, 'r').convert("RGBA").resize((197, 278))
            icon_coords = get_position_text(card_type, "Planet", "First Icon")
            icon_coords = (icon_coords[0],
                           icon_coords[1] + num_icons * get_position_text(card_type, "Planet", "Icon Spacing"))
            resulting_img.paste(material_img, icon_coords, material_img)
            num_icons += 1
        if c == "B":
            technology_src = "cards/custom_card_creator/card_srcs/Planet/Icons/Technology.png"
            technology_img = Image.open(technology_src, 'r').convert("RGBA").resize((197, 278))
            icon_coords = get_position_text(card_type, "Planet", "First Icon")
            icon_coords = (icon_coords[0],
                           icon_coords[1] + num_icons * get_position_text(card_type, "Planet", "Icon Spacing"))
            resulting_img.paste(technology_img, icon_coords, technology_img)
            num_icons += 1
        if c == "G":
            strongpoint_src = "cards/custom_card_creator/card_srcs/Planet/Icons/Strongpoint.png"
            strongpoint_img = Image.open(strongpoint_src, 'r').convert("RGBA").resize((197, 278))
            icon_coords = get_position_text(card_type, "Planet", "First Icon")
            icon_coords = (icon_coords[0],
                           icon_coords[1] + num_icons * get_position_text(card_type, "Planet", "Icon Spacing"))
            resulting_img.paste(strongpoint_img, icon_coords, strongpoint_img)
            num_icons += 1
        if c in ["R", "G", "B"] and num_icons > 1:
            connector_src = "cards/custom_card_creator/card_srcs/Planet/Icons/Icon_Join.jpg"
            connector_img = Image.open(connector_src, 'r').convert("RGBA").resize((74, 45))
            icon_coords = get_position_text(card_type, "Planet", "First Join")
            print(icon_coords)
            icon_coords = (icon_coords[0], icon_coords[1] + (num_icons - 1)
                           * get_position_text(card_type, "Planet", "Join Spacing"))
            print(icon_coords)
            resulting_img.paste(connector_img, icon_coords, connector_img)
    resulting_img.save(output_dir, "PNG")
    return True


def process_submitted_card(name, card_type, text, faction, traits, output_dir,
                           attack="0", health="0", command="0", cost="0",
                           starting_cards="7", starting_resources="7",
                           loyalty="Common", shield_value="0",
                           input_src=""):
    text_src = "cards/custom_card_creator/card_srcs/" + faction + "/" + card_type + "/Text.png"
    if not os.path.exists(text_src):
        return False
    card_art_src = input_src
    expansion_icon_dirs = "cards/custom_card_creator/current_card_info/expansion_icon/"
    dirs_expansion = os.listdir(expansion_icon_dirs)
    if not dirs_expansion:
        return False
    random.shuffle(dirs_expansion)
    expansion_icon_src = "cards/custom_card_creator/current_card_info/expansion_icon/" + dirs_expansion[0]
    first_command_src = "cards/custom_card_creator/card_srcs/" + faction + "/" + card_type + "/First_Command.png"
    command_end_src = "cards/custom_card_creator/card_srcs/" + faction + "/" + card_type + "/Command_End.png"
    extra_command_src = "cards/custom_card_creator/card_srcs/" + faction + "/" + card_type + "/Extra_Command_Icon.png"
    resulting_img = Image.new("RGBA", (1440, 2052))
    dirs_art = os.listdir(card_art_src)
    if not dirs_art:
        return False
    random.shuffle(dirs_art)
    card_art_img = Image.open(card_art_src + dirs_art[0], 'r').convert("RGBA")
    if card_type == "Warlord":
        card_art_img = card_art_img.resize((1440, 2052))
    else:
        card_art_img = card_art_img.resize((1440, 1500))
    resulting_img.paste(card_art_img, get_position_text(card_type, faction, "Art"))
    text_resize_amount = (1440, 2052)
    required_line_length = 1240
    if card_type != "Planet":
        required_line_length = card_types_dictionary_positions[card_type][faction]["Text Length"]
    text_img = Image.open(text_src, 'r').convert("RGBA")
    text_img = text_img.resize(text_resize_amount)
    resulting_img.paste(text_img, get_position_text(card_type, faction, "Text Box"), text_img)
    expansion_icon_img = Image.open(expansion_icon_src, 'r').convert("RGBA").resize((55, 55))
    resulting_img.paste(expansion_icon_img, get_position_text(card_type, faction, "Expansion Icon"), expansion_icon_img)
    add_name_to_card(card_type, name, resulting_img)
    add_traits_to_card(card_type, traits, resulting_img)
    add_text_to_image(resulting_img, text, get_position_text(card_type, faction, "Text"),
                      line_length=required_line_length)
    deepstrike = False
    if "Deep Strike (" in text:
        deepstrike = True
    if card_type in ["Army", "Support", "Event", "Attachment"]:
        add_text_to_image(
            resulting_img, cost, get_position_text(card_type, faction, "Cost"),
            font_src="cards/custom_card_creator/fonts/Jawbreak/BoxTube Labs - Jawbreak Sans.otf",
            font_size=120, color=(0, 0, 0), deepstrike=deepstrike
        )
    if card_type in ["Army", "Warlord", "Synapse"]:
        add_text_to_image(
            resulting_img, attack, get_position_text(card_type, faction, "Attack"),
            font_src="cards/custom_card_creator/fonts/Jawbreak/BoxTube Labs - Jawbreak Sans.otf",
            font_size=120, color=(255, 255, 255)
        )
        add_text_to_image(
            resulting_img, health, get_position_text(card_type, faction, "Health"),
            font_src="cards/custom_card_creator/fonts/Jawbreak/BoxTube Labs - Jawbreak Sans.otf",
            font_size=120, color=(0, 0, 0)
        )
    if card_type in ["Army", "Synapse"] and faction != "Neutral":
        try:
            add_command_icons(command, first_command_src, extra_command_src,
                              command_end_src, resulting_img, faction, card_type)
        except ValueError:
            pass
    if card_type == "Warlord":
        add_text_to_image(
            resulting_img, starting_cards, get_position_text(card_type, faction, "Cards"),
            font_size=168, color=(0, 0, 0)
        )
        add_text_to_image(
            resulting_img, starting_resources, get_position_text(card_type, faction, "Resources"),
            font_size=168, color=(243, 139, 18)
        )
    if card_type in ["Army", "Support", "Event", "Attachment"]:
        if (loyalty == "Loyal" or loyalty == "Signature") and faction != "Neutral":
            loyalty_src = "cards/custom_card_creator/card_srcs/" + faction + "/Loyalty/" + loyalty + ".png"
            loyalty_img = Image.open(loyalty_src, 'r').convert("RGBA")
            resize_loyalty = (127, 84)
            if faction == "Tau":
                resize_loyalty = (147, 184)
            loyalty_img = loyalty_img.resize(resize_loyalty)
            resulting_img.paste(loyalty_img, get_position_loyalty(faction, card_type), loyalty_img)
    if card_type in ["Event", "Attachment"]:
        shield_value = int(shield_value)
        if shield_value > 0:
            shield_src = "cards/custom_card_creator/card_srcs/" + faction + "/Shield/Shield_Icon.png"
            shield_icon_img = Image.open(shield_src, 'r').convert("RGBA")
            shield_icon_img = shield_icon_img.resize((221, 101))
            starting_position_shield = get_position_text(card_type, faction, "Shield")
            for _ in range(shield_value):
                resulting_img.paste(shield_icon_img, starting_position_shield, shield_icon_img)
                starting_position_shield = (starting_position_shield[0], starting_position_shield[1] + 100)
    resulting_img.save(output_dir, "PNG")
    return True


def ajax_creator(request):
    if request.method == 'POST':
        try:
            card_name = request.POST.get('card_name')
            text = request.POST.get('text')
            card_traits = request.POST.get('traits')
            card_type = request.POST.get('card_type')
            faction = request.POST.get('faction')
            loyalty = request.POST.get('loyalty')
            cost = request.POST.get('cost')
            command = request.POST.get('command')
            attack = request.POST.get('attack')
            health = request.POST.get('health')
            shield = request.POST.get('shield')
            starting_cards = request.POST.get('starting_cards')
            starting_resources = request.POST.get('starting_resources')
            cards_value = request.POST.get('cards_value')
            resources_value = request.POST.get('resources_value')
            icons = request.POST.get('icons')
            username = request.user.username
            if not username:
                username = "Anonymous"
            key_code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                               for _ in range(16))
            output_dir = "media/resulting_images/" + username
            if not os.path.exists("media/resulting_images/"):
                os.mkdir("media/resulting_images/")
            if not os.path.exists("media/card_img_srcs/"):
                os.mkdir("media/card_img_srcs/")
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            for filename in os.listdir(output_dir):
                file_path = os.path.join(output_dir, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            output_src = output_dir + "/" + key_code + ".png"
            cwd = os.getcwd()
            input_src = "cards/custom_card_creator/current_card_info/src_img/"
            username = request.user.username
            if username:
                if os.path.exists(cwd + "/media/card_img_srcs/" + username):
                    file_names = os.listdir(cwd + "/media/card_img_srcs/" + username)
                    if file_names:
                        input_src = cwd + "/media/card_img_srcs/" + username + "/"
            if card_type == "Planet":
                if process_submitted_planet_card(card_name, card_type, text,
                                                 cards_value, resources_value, icons, output_src, input_src):
                    return JsonResponse({'message': 'SUCCESS', 'new_src': output_src})
            else:
                if process_submitted_card(card_name, card_type, text, faction, card_traits, output_src,
                                          attack=attack, health=health, command=command, cost=cost,
                                          starting_cards=starting_cards, starting_resources=starting_resources,
                                          loyalty=loyalty, shield_value=shield, input_src=input_src):
                    return JsonResponse({'message': 'SUCCESS', 'new_src': output_src})
            return JsonResponse(
                {'message': 'Failed - invalid parameters.', 'new_src': '/static/images/CardImages/Nazdreg.jpg'})
        except Exception as e:
            print(e)
        return JsonResponse(
            {'message': 'Failed - error during processing.', 'new_src': '/static/images/CardImages/Nazdreg.jpg'})
    return render(request, 'cards/card_creator.html', {})


def upload_card(request):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    return render(request, 'cards/upload_card.html', {
        "light_dark_toggle": light_dark_toggle
    })


def simple_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        if request.user.is_authenticated:
            username = request.user.username
            files = request.FILES['file']
            print('got here')
            cwd = os.getcwd()
            destination = cwd + "/media/card_img_srcs/"
            destination = destination + username
            if os.path.exists(destination):
                for filename in os.listdir(destination):
                    file_path = os.path.join(destination, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
            key_code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                               for _ in range(16))
            destination = "card_img_srcs/" + username + "/" + key_code + ".jpg"
            print(destination)
            file_data = files.read()
            print(len(file_data))
            fs = FileSystemStorage()
            file_name = fs.save(destination, files)
    return redirect("/cards/card_creator/")


# View to handle the Ajax request
def ajax_view(request):
    if request.method == 'POST':
        card_names = []
        search = request.POST.get('search')
        redirect_enabled = request.POST.get('redirect-enabled')
        if search.islower():
            if search in lower_case_dict and redirect_enabled == "Yes":
                image_name = lower_case_dict[search].image_name
                return JsonResponse({'message': "REDIRECT", 'cards': card_names, 'image_names': [image_name]})
            elif search in lower_case_planet_dict and redirect_enabled == "Yes":
                image_name = lower_case_planet_dict[search].image_name
                return JsonResponse({'message': "REDIRECT", 'cards': card_names, 'image_names': [image_name]})
        if search in cards_dict and redirect_enabled == "Yes":
            image_name = cards_dict[search].image_name
            return JsonResponse({'message': "REDIRECT", 'cards': card_names, 'image_names': [image_name]})
        elif search in planets_dict and redirect_enabled == "Yes":
            image_name = planets_dict[search].image_name
            return JsonResponse({'message': "REDIRECT", 'cards': card_names, 'image_names': [image_name]})
        faction = request.POST.get('faction')
        traits = request.POST.get('traits')
        text = request.POST.get('text')
        card_type = request.POST.get('card_type')
        shields = request.POST.get('shields')
        keyword_card = request.POST.get('keyword')
        view_as = request.POST.get('view-as')
        cycle = request.POST.get('cycle')
        warpack = request.POST.get('war-pack')
        if card_type == "Planet" and view_as != "Rows Mini":
            filtered_df = planet_df
            if search.islower():
                filtered_df = filtered_df[filtered_df['name'].str.contains("(?i)" + search)]
            else:
                filtered_df = filtered_df[filtered_df['name'].str.contains(search)]
            if text.islower():
                filtered_df = filtered_df[filtered_df['text'].str.contains("(?i)" + text)]
            else:
                filtered_df = filtered_df[filtered_df['text'].str.contains(text)]
            sector = request.POST.get('sector')
            filtered_df = filtered_df[filtered_df['sector'].str.contains(sector)]
            card_names = filtered_df['name'].to_list()
            image_names = filtered_df['image name'].to_list()
            return JsonResponse({'message': "", 'cards': card_names, 'image_names': image_names})
        min_cost = None
        max_cost = None
        min_command = -1
        max_command = -1
        min_attack = -1
        max_attack = -1
        min_health = -1
        max_health = -1
        filtered_df = df
        order_by = request.POST.get('order')
        asc = request.POST.get('asc')
        if view_as == "Rows Mini":
            warlord_name = request.POST.get('warlord_name')
            ally_faction = request.POST.get('ally_faction')
            special_factions = request.POST.get('special_factions')
            special_factions = ast.literal_eval(special_factions)
            special_enabled = request.POST.get('special_enabled')
            special_enabled = ast.literal_eval(special_enabled)
            special_types = request.POST.get('special_types')
            special_types = ast.literal_eval(special_types)
            special_types_enabled = request.POST.get('special_types_enabled')
            special_types_enabled = ast.literal_eval(special_types_enabled)
            warlord = FindCard.find_card(warlord_name, card_array, cards_dict)
            if special_factions:
                if len(special_factions) == len(special_enabled):
                    extra_faction_filter = []
                    for i in range(len(special_factions)):
                        if special_enabled[i] == "Y":
                            extra_faction_filter.append(special_factions[i])
                    if extra_faction_filter:
                        filtered_df = filtered_df[filtered_df['faction'].isin(extra_faction_filter)]
            if special_types:
                if len(special_types) == len(special_types_enabled):
                    extra_card_type_filter = []
                    for i in range(len(special_types)):
                        if special_types_enabled[i] == "Y":
                            extra_card_type_filter.append(special_types[i])
                    if extra_card_type_filter:
                        filtered_df = filtered_df[filtered_df['card type'].isin(extra_card_type_filter)]
            if warlord_name == "Gorzod":
                filtered_df = filtered_df[(((filtered_df['faction'] == "Space Marines") &
                                            (filtered_df['loyalty'] == "Common") &
                                            (filtered_df['traits'].str.contains("Vehicle"))) |
                                           ((filtered_df['faction'] == "Astra Militarum") &
                                            (filtered_df['loyalty'] == "Common") &
                                            (filtered_df['traits'].str.contains("Vehicle"))) |
                                           ((filtered_df['faction'] == "Orks") &
                                            (filtered_df['loyalty'] != "Signature"))) |
                                          (filtered_df['faction'] == "Neutral")]
            elif warlord.get_faction() == "Necrons":
                valid_necrons_enslavement = ["Astra Militarum", "Space Marines", "Tau",
                                             "Eldar", "Dark Eldar", "Chaos", "Orks"]
                filtered_df = filtered_df[(((filtered_df['faction'] == warlord.get_faction()) &
                                            (filtered_df['loyalty'] != "Signature")) |
                                           ((filtered_df['faction'].isin(valid_necrons_enslavement)) &
                                            (filtered_df['loyalty'] == "Common")) &
                                           (filtered_df['card type'] == "Army")) |
                                          (filtered_df['faction'] == "Neutral")]
            elif warlord.get_faction() == "Tyranids" and warlord.get_name() != "Termagant":
                filtered_df = filtered_df[(((filtered_df['faction'] == warlord.get_faction()) &
                                            (filtered_df['loyalty'] != "Signature"))) |
                                          ((filtered_df['faction'] == "Neutral") &
                                           (filtered_df['card type'] != "Army"))]
            elif warlord_name and ally_faction:
                filtered_df = filtered_df[(((filtered_df['faction'] == warlord.get_faction()) &
                                            (filtered_df['loyalty'] != "Signature")) |
                                           ((filtered_df['faction'] == ally_faction) &
                                            (filtered_df['loyalty'] == "Common"))) |
                                          (filtered_df['faction'] == "Neutral")]
            elif warlord_name:
                warlord = FindCard.find_card(warlord_name, card_array, cards_dict)
                filtered_df = filtered_df[(((filtered_df['faction'] == warlord.get_faction()) &
                                            (filtered_df['loyalty'] != "Signature"))) |
                                          (filtered_df['faction'] == "Neutral")]
            if warlord_name == "Yvraine":
                filtered_df = filtered_df[((filtered_df['faction'] != "Chaos") |
                                           (~filtered_df['traits'].str.contains("Elite")))]
        if order_by != "None":
            ascending = False
            if asc == "Ascending":
                ascending = True
            order_by = order_by.lower()
            if order_by in filtered_df.columns:
                if order_by == "cycle":
                    filtered_df = filtered_df.sort_values(by='cycle', key=sorter_cycles, kind="stable")
                elif order_by == "war pack":
                    filtered_df = filtered_df.sort_values(by='war pack', key=sorter_warpacks, kind="stable")
                else:
                    filtered_df = filtered_df.sort_values(by=[order_by], ascending=ascending, kind="stable")
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
        if traits:
            filtered_df = filtered_df[filtered_df['traits'].str.contains(traits)]
        if search is not None:
            if search.islower():
                try:
                    filtered_df = filtered_df[filtered_df['name'].str.contains("(?i)" + search)]
                except Exception as e:
                    print(e)
            else:
                filtered_df = filtered_df[filtered_df['name'].str.contains(search)]
        if text is not None:
            if text.islower():
                try:
                    filtered_df = filtered_df[filtered_df['text'].str.contains("(?i)" + text)]
                except Exception as e:
                    print(e)
            else:
                filtered_df = filtered_df[filtered_df['text'].str.contains(text)]
        if keyword_card != "None":
            filtered_df = filtered_df[filtered_df['keywords'].str.contains(keyword_card)]
        if cycle:
            filtered_df = filtered_df.loc[filtered_df['cycle'] == cycle]
        if warpack:
            filtered_df = filtered_df.loc[filtered_df['war pack'] == warpack]
        if shields != "-1":
            shields = int(shields)
            filtered_df = filtered_df.loc[filtered_df['shields'] == shields]
        if faction != "None":
            filtered_df = filtered_df.loc[filtered_df['faction'] == faction]
        if loyalty != "None":
            filtered_df = filtered_df.loc[filtered_df['loyalty'] == loyalty]
        if card_type != "None":
            filtered_df = filtered_df.loc[filtered_df['card type'] == card_type]
        if min_cost is not None:
            filtered_df = filtered_df.loc[filtered_df['cost'] >= min_cost]
        if max_cost is not None:
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
        attack_vals = filtered_df['attack'].to_list()
        health_vals = filtered_df['health'].to_list()
        cost_vals = filtered_df['cost'].to_list()
        command_vals = filtered_df['command'].to_list()
        shield_vals = filtered_df['shields'].to_list()
        for i in range(len(attack_vals)):
            if attack_vals[i] == -1:
                attack_vals[i] = "-"
            if health_vals[i] == -1:
                health_vals[i] = "-"
            if cost_vals[i] == -1:
                cost_vals[i] = "-"
            if command_vals[i] == -1:
                command_vals[i] = "-"
            if shield_vals[i] == 0:
                shield_vals[i] = "-"
        message = f'Faction, {faction}'
        return JsonResponse({'message': message, 'cards': card_names, 'image_names': image_names,
                             'loyalties': loyalties, 'card_types': card_types, 'factions': factions,
                             'attack': attack_vals, 'health': health_vals, 'cost': cost_vals,
                             'command': command_vals, "shield": shield_vals})
    return JsonResponse({'message': 'Invalid request'})


def rate_card(request, card_name, rating_value):
    username = request.user.username
    try:
        rating_value = int(rating_value)
    except:
        return HttpResponseRedirect("/cards/" + card_name + "/")
    if rating_value < 0 or rating_value > 5 or not username:
        return HttpResponseRedirect("/cards/" + card_name + "/")
    directory = os.getcwd()
    ratings_file = directory + "/cards/ratings/" + card_name + ".csv"
    if not os.path.exists(directory + "/cards/ratings/"):
        os.makedirs(directory + "/cards/ratings/", exist_ok=True)
    if not os.path.exists(ratings_file):
        new_df = pd.DataFrame({'Name': [], 'Rating': []})
        new_df.to_csv(ratings_file, header=True, index=False)
    new_df = pd.read_csv(ratings_file)
    create_new_rating = True
    if username in new_df["Name"].values:
        current_rating = new_df.loc[new_df["Name"] == username, "Rating"]
        if int(current_rating.iloc[0]) == rating_value:
            create_new_rating = False
        new_df = new_df[new_df["Name"] != username]
        if not create_new_rating:
            new_df.to_csv(ratings_file, header=True, index=False)
    if create_new_rating:
        new_row = pd.DataFrame({'Name': [username], 'Rating': [rating_value]})
        new_df = pd.concat([new_df, new_row], ignore_index=True)
        new_df.to_csv(ratings_file, header=True, index=False)
    return HttpResponseRedirect("/cards/" + card_name + "/")


def card_data(request, card_name):
    username = request.user.username
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    directory = os.getcwd()
    target_directory = directory + "/cards/comments/" + card_name + "/"
    ratings_file = directory + "/cards/ratings/" + card_name + ".csv"
    print("Request Received for:", card_name)
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
    if card_name not in images_dict:
        return render(request, 'cards/index.html', {"light_dark_toggle": light_dark_toggle})
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
    cycle_text = card.get_cycle_info_as_text()
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
    errata_card_name = ""
    errata_faction = ""
    errata_loyalty = ""
    errata_card_type = ""
    errata_traits = ""
    errata_full_text = ""
    errata_cycle_text = ""
    errata_cost = -1
    errata_shields = -1
    errata_command = -1
    errata_bloodied_text = ""
    errata_bloodied_attack = -1
    errata_bloodied_health = -1
    errata_attack = -1
    errata_health = -1
    errata_is_unit = "False"
    sig_squad = []
    sig_squad_links = []
    if card_type == "Warlord":
        try:
            sig_squad_raw = card.signature_squad
            for a in range(len(sig_squad_raw)):
                num = int(sig_squad_raw[a][0])
                for _ in range(num):
                    sig_squad.append(sig_squad_raw[a][3:])
        except:
            pass
    for a in range(len(sig_squad)):
        sig_squad_links.append(convert_name_to_hyperlink(sig_squad[a]))
        sig_squad[a] = convert_name_to_img_src(sig_squad[a])
    if card_name in apoka_errata_dict:
        card = apoka_errata_dict[card_name]
        errata_card_name = card.get_name()
        errata_cycle_text = card.get_cycle_info_as_text()
        errata_faction = card.get_faction()
        errata_loyalty = card.get_loyalty()
        errata_card_type = card.get_card_type()
        errata_traits = card.get_traits()
        errata_full_text = card.get_text()
        errata_cost = card.get_cost()
        errata_shields = str(card.get_shields())
        if card.is_unit:
            if errata_card_type != "Warlord":
                errata_card_type = errata_card_type + " Unit"
                errata_command = str(card.command)
            else:
                errata_bloodied_text = card.bloodied_text
                errata_bloodied_attack = card.bloodied_attack
                errata_bloodied_health = card.bloodied_health
            errata_is_unit = "True"
            errata_attack = str(card.attack)
            errata_health = str(card.health)
        errata_text = "There is Errata"
    if original_card_name in banned_cards:
        ban_text = "Banned"
    names_comments = []
    times_comments = []
    comments = []
    comment_ids = []
    no_comments = True
    if card_type == "Planet":
        text = card.get_sector_as_text() + card.get_icons_as_text() + card.get_winnings_as_text() + \
               card.get_commit_text_as_text() + text
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
    if not os.path.exists(directory + "/cards/ratings/"):
        os.makedirs(directory + "/cards/ratings/", exist_ok=True)
    if not os.path.exists(ratings_file):
        new_df = pd.DataFrame({'Name': [], 'Rating': []})
        new_df.to_csv(ratings_file, header=True, index=False)
    own_ratings = [False, False, False, False, False]
    has_rated = False
    new_df = pd.read_csv(ratings_file)
    average_rating = new_df["Rating"].mean()
    if pd.isna(average_rating):
        average_rating = 0
    average_rating = int(round(average_rating))
    ratings = []
    for _ in range(average_rating):
        ratings.append(True)
    for _ in range(5 - average_rating):
        ratings.append(False)
    if username in new_df["Name"].values:
        current_rating = new_df.loc[new_df["Name"] == username, "Rating"]
        current_rating = int(current_rating.iloc[0])
        own_ratings = []
        has_rated = True
        for _ in range(current_rating):
            own_ratings.append(True)
        for _ in range(5 - current_rating):
            own_ratings.append(False)
    num_ratings = new_df.shape[0]
    my_comments = zip(names_comments, times_comments, comments, comment_ids)
    sig_squad = zip(sig_squad, sig_squad_links)
    own_ratings = zip(own_ratings, [1, 2, 3, 4, 5])
    rotate = False
    if card_type == "Planet" or "Pledge" in traits:
        rotate = True
    return render(request, "cards/card_data.html",
                  {"card_name": original_card_name, "image_name": image_name, "text": text,
                   "card_type": card_type, "cost": cost, "command": command, "attack": attack, "health": health,
                   "is_unit": is_unit, "loyalty": loyalty, "faction": faction, "traits": traits,
                   "ban_text": ban_text, "errata_text": errata_text, "shields": shields,
                   "bloodied_attack": bloodied_attack, "bloodied_health": bloodied_health,
                   "bloodied_text": bloodied_text, "comments": my_comments, "noc": no_comments,
                   "errata_card_name": errata_card_name, "errata_faction": errata_faction,
                   "errata_loyalty": errata_loyalty, "errata_card_type": errata_card_type,
                   "errata_traits": errata_traits, "errata_full_text": errata_full_text,
                   "errata_cost": errata_cost, "errata_shields": errata_shields,
                   "errata_command": errata_command, "errata_bloodied_text": errata_bloodied_text,
                   "errata_bloodied_attack": errata_bloodied_attack, "errata_bloodied_health": errata_bloodied_health,
                   "errata_attack": errata_attack, "errata_health": errata_health, "errata_is_unit": errata_is_unit,
                   "light_dark_toggle": light_dark_toggle, "cycle_text": cycle_text,
                   "errata_cycle_text": errata_cycle_text, "sig_squad": sig_squad, "rotate": rotate,
                   "ratings": ratings, "own_ratings": own_ratings, "num_ratings": num_ratings, "has_rated": has_rated})
