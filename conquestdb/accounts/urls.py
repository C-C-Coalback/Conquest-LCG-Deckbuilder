from django.urls import path

from .views import SignUpView
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("settings/", views.user_settings, name="user_settings"),
]
