# -*- coding: utf-8 -*-
import logging
import os

from django.conf import settings
from django.core.management import BaseCommand

from album.models import Template


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        b_path = os.path.join(settings.BASE_DIR, 'album/templates/album/web/album_templates')
        filenames = os.listdir(b_path)
        path_names = [filename[:-5] for filename in filenames]

        Template.objects.filter(path_name__in=path_names, public=False).update(public=True)



