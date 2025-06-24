from django.urls import path

from . import views

urlpatterns = [
    path("", views.decks, name="decks"),
    path("<str:card_name>/", views.deck_data, name="deck_data"),
]
