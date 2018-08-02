
from django.db.models import Count

from album import models as album_models


def get_or_create_default_album(user):
    album = album_models.Album.objects.filter(
        user=user,
    ).annotate(
        picture_count=Count('pictures__id'),
    ).filter(
        picture_count=0
    ).first()

    if not album:
        album = album_models.Album.objects.create(
            user=user
        )
    return album