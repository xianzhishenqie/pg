
from django.urls import path, re_path

from . import api
from . import views


viewsets = (
    api.TemplateTagViewSet,
    api.TemplateViewSet,
    api.MusicTagViewSet,
    api.MusicViewSet,
    api.AlbumViewSet,
    api.PublicAlbumViewSet,
)


urlpatterns = [
    path('albums/', views.album_list_page, name='album_list'),
    path('albums/<int:pk>/display/', views.album_display_page, name='album_display'),
]
