from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
import light_dark_dict


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def user_settings(request):
    if request.method == "POST":
        light_dark = request.POST.get("light")
        if light_dark != "None":
            light_dark_dict.update_light_mode(request.user.username, light_dark)
    light_dark_toggle = light_dark_dict.get_light_mode(request.user.username)
    return render(request, "registration/settings.html", {"light_dark_toggle": light_dark_toggle})
