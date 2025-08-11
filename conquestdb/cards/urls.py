from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ajax/", views.ajax_view, name="ajax_view"),
    path("<str:card_name>/", views.card_data, name="card_data"),
    path("ratings/<str:card_name>/<str:rating_value>/", views.rate_card, name="rate_card")
]
