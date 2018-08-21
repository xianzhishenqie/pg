import logging
import random

from django.db.models import Count

from album import models as album_models


logger = logging.getLogger(__name__)


def random_template():
    random_index = random.choice(range(0, album_models.Template.objects.count()))
    template = album_models.Template.objects.all()[random_index: random_index + 1][0]
    return template


def get_or_create_default_album(user):
    album = album_models.Album.objects.filter(
        user=user,
    ).annotate(
        picture_count=Count('pictures__id'),
    ).filter(
        picture_count=0
    ).first()

    if not album:
        template = random_template()
        album = album_models.Album.objects.create(
            name='我用照片制作了一个相册,打开看看！',
            desc='这个相册，送给你',
            user=user,
            template=template,
            music=template.default_music,
        )
    return album


def fix_empty_template_album(album):
    template = random_template()
    album.template = template
    if not album.music:
        album.music = template.default_music
    try:
        album.save()
    except Exception as e:
        logger.error('save album[%s] error', album.id)