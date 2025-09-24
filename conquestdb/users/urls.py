from django.urls import path

from . import views

urlpatterns = [
    path("", views.own_user, name="index"),
    path("<str:chosen_user>/", views.target_user, name="target_user")
]
