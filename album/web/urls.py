
from django.urls import path

from . import api
from . import views


viewsets = (
    api.MusicTagViewSet,
    api.MusicViewSet,
    api.AlbumViewSet,
)


urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('album/<int:pk>/', views.album_page, name='album'),
]
