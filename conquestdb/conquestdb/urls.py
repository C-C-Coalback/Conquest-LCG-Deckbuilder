"""
URL configuration for conquestdb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.views.generic.base import TemplateView
from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("cards/", include("cards.urls")),
    path("decks/", include("decks.urls")),
    path("users/", include("users.urls")),
    path("api/", include("api.urls")),
    path("play_formats/", views.play_formats_page, name="play_formats"),
    path("ban_lists/", views.ban_lists_page, name="ban_lists"),
    path("recent_reviews/", views.recent_reviews, name="recent_reviews"),
    path("recent_reviews/<int:page_num>/", views.recent_reviews_page, name="recent_reviews_page"),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path("", views.home_page, name="home"),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('accounts/', include('django.contrib.auth.urls')),
]
