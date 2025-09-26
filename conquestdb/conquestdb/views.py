from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
import os
import pandas as pd
import light_dark_dict


def convert_name_to_hyperlink(card_name):
    card_name = card_name.replace("\"", "")
    card_name = card_name.replace(" ", "_")
    card_name = card_name.replace("'idden_Base", "idden_Base")
    card_name = "/cards/" + card_name
    return card_name


def simple_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        if request.user.is_authenticated:
            username = request.user.username
            files = request.FILES['file']
            print('got here')
            cwd = os.getcwd()
            destination = cwd + "/media/"
            destination = destination + username + ".jpg"
            if os.path.exists(destination):
                os.remove(destination)
            destination = username + ".jpg"
            print(destination)
            file_data = files.read()
            print(len(file_data))
            fs = FileSystemStorage()
            file_name = fs.save(destination, files)
            # img = Image.open(files)
            # img.save(destination)
    return redirect("/")


def home_page(request):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    return render(request, "home.html", {"light_dark_toggle": light_dark_toggle})


def recent_reviews_page(request, page_num):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    cwd = os.getcwd()
    target_directory = cwd + "/cards/comments/"
    comments_contents = []
    comments_users = []
    comments_dates = []
    card_names = []
    card_links = []
    max_comments = 5
    if page_num < 1:
        page_num = 1
    if os.path.exists(target_directory):
        for card_name in os.listdir(target_directory):
            if card_name:
                second_target_directory = target_directory + "/" + card_name
                for comment_file in os.listdir(second_target_directory):
                    with open(second_target_directory + "/" + comment_file) as f:
                        file_contents = f.read()
                        if file_contents:
                            split_content = file_contents.split(sep="\n")
                            comments_users.append(split_content[0])
                            comments_dates.append(split_content[1])
                            comments_contents.append(split_content[2])
                            card_names.append(card_name.replace("_", " "))
                            card_links.append(convert_name_to_hyperlink(card_name))
    data = {
        "comments_contents": comments_contents,
        "comments_users": comments_users,
        "comments_dates": comments_dates,
        "card_names": card_names,
        "card_links": card_links
    }
    df = pd.DataFrame(data=data)
    df = df.sort_values(by="comments_dates", ascending=False)
    comments_contents = df["comments_contents"]
    comments_users = df["comments_users"]
    comments_dates = df["comments_dates"]
    card_names = df["card_names"]
    card_links = df["card_links"]
    if len(comments_contents) > max_comments:
        comments_contents = comments_contents[(max_comments * (page_num - 1)):(max_comments * page_num)]
        comments_users = comments_users[(max_comments * (page_num - 1)):(max_comments * page_num)]
        comments_dates = comments_dates[(max_comments * (page_num - 1)):(max_comments * page_num)]
        card_names = card_names[(max_comments * (page_num - 1)):(max_comments * page_num)]
        card_links = card_links[(max_comments * (page_num - 1)):(max_comments * page_num)]
    sent_comments = zip(comments_contents, comments_users, comments_dates, card_names, card_links)
    return render(request, "recent_reviews.html", {"light_dark_toggle": light_dark_toggle,
                                                   "sent_comments": sent_comments})


def recent_reviews(request):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    cwd = os.getcwd()
    target_directory = cwd + "/cards/comments/"
    comments_contents = []
    comments_users = []
    comments_dates = []
    card_names = []
    card_links = []
    max_comments = 3
    if os.path.exists(target_directory):
        for card_name in os.listdir(target_directory):
            if card_name:
                second_target_directory = target_directory + "/" + card_name
                for comment_file in os.listdir(second_target_directory):
                    with open(second_target_directory + "/" + comment_file) as f:
                        file_contents = f.read()
                        if file_contents:
                            split_content = file_contents.split(sep="\n")
                            comments_users.append(split_content[0])
                            comments_dates.append(split_content[1])
                            comments_contents.append(split_content[2])
                            card_names.append(card_name.replace("_", " "))
                            card_links.append(convert_name_to_hyperlink(card_name))
    data = {
        "comments_contents": comments_contents,
        "comments_users": comments_users,
        "comments_dates": comments_dates,
        "card_names": card_names,
        "card_links": card_links
    }
    df = pd.DataFrame(data=data)
    df = df.sort_values(by="comments_dates", ascending=False)
    comments_contents = df["comments_contents"]
    comments_users = df["comments_users"]
    comments_dates = df["comments_dates"]
    card_names = df["card_names"]
    card_links = df["card_links"]
    if len(comments_contents) > max_comments:
        comments_contents = comments_contents[:max_comments]
        comments_users = comments_users[:max_comments]
        comments_dates = comments_dates[:max_comments]
        card_names = card_names[:max_comments]
        card_links = card_links[:max_comments]
    sent_comments = zip(comments_contents, comments_users, comments_dates, card_names, card_links)
    return render(request, "recent_reviews.html", {"light_dark_toggle": light_dark_toggle,
                                                   "sent_comments": sent_comments})


def play_formats_page(request):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    return render(request, "play_formats.html", {"light_dark_toggle": light_dark_toggle})


def ban_lists_page(request):
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    return render(request, "ban_lists.html", {"light_dark_toggle": light_dark_toggle})
