# -*- coding: utf-8 -*-
import logging

from django.core.management import BaseCommand
from we.utils.menu import create_menus

from album import setting


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        ret = create_menus(setting.APP_MENUS)
        logger.info(ret)

