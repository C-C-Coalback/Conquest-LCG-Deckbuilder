from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
import os
import light_dark_dict


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
