from django.urls import path

from . import views

urlpatterns = [
    path("", views.nothing, name="nothing"),
    path("tts/<str:deck_key>/", views.request_deck, name="request_deck"),
    path("tts/", views.tts_welcome, name="tts_welcome"),
]
