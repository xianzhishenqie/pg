
from django.urls import path, re_path

from . import api
from . import views


viewsets = (
    api.MusicTagViewSet,
    api.MusicViewSet,
)


urlpatterns = [
    path('musics/', views.music_manage_page, name='music_manage'),
]
