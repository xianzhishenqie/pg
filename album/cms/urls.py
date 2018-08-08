
from django.urls import path, re_path

from . import api
from . import views


viewsets = (
    api.MusicTagViewSet,
    api.MusicViewSet,
    api.AlbumViewSet,
)


urlpatterns = [
    path('albums/', views.album_manage_page, name='album_manage'),
    path('musics/', views.music_manage_page, name='music_manage'),
]
