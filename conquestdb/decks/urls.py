from django.urls import path

from . import views

urlpatterns = [
    path("", views.decks, name="decks"),
    path("create_deck/", views.create_deck, name="create_deck"),
    path("my_decks/", views.my_decks, name="my_decks"),
    path("ajax/", views.ajax_view, name="ajax"),
    path("<str:deck_name>/", views.deck_data, name="deck_data"),
]
