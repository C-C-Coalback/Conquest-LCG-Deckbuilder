from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ajax/", views.ajax_view, name="ajax_view"),
    path("ajax_creator/", views.ajax_creator, name="ajax_creator"),
    path("card_creator/", views.card_creator, name="card_creator"),
    path('upload_card/', views.upload_card, name='upload_card'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path("<str:card_name>/", views.card_data, name="card_data"),
    path("ratings/<str:card_name>/<str:rating_value>/", views.rate_card, name="rate_card")
]
