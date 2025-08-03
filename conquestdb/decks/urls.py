from django.urls import path

from . import views

urlpatterns = [
    path("", views.decks, name="decks"),
    path("create_deck/<str:deck_key>/", views.modify_deck, name="modify_deck"),
    path("delete_deck/<str:deck_key>/", views.delete_deck, name="delete_deck"),
    path("publish_deck/<str:deck_key>/", views.publish_deck, name="publish_deck"),
    path("retract_deck/<str:deck_key>/", views.retract_deck, name="retract_deck"),
    path("copy_deck/<str:deck_key>/", views.copy_published_deck, name="copy_deck"),
    path("create_deck/", views.create_deck, name="create_deck"),
    path("my_decks/<int:page_num>/", views.my_decks_page, name="my_decks_page"),
    path("my_decks/", views.my_decks, name="my_decks"),
    path("published_decks/<int:page_num>/", views.published_decks_page, name="published_decks_page"),
    path("published_decks/", views.published_decks, name="published_decks"),
    path("ajax/", views.ajax_view, name="ajax"),
    path("<str:deck_creator>/<str:deck_key>/advanced_deck_details/", views.advanced_deck_details, name="adv_deck"),
    path("<str:deck_creator>/<str:deck_key>/", views.deck_data, name="deck_data"),
    path("<str:deck_creator>/", views.user_deck_data, name="user_decks_data"),
]
