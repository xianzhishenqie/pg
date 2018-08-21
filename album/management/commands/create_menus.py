import logging

from django.core.management import BaseCommand
from we.utils.menu import create_menus

from album import setting


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('app_id', nargs='+', type=str)

    def handle(self, *args, **options):
        app_id = options.get('app_id')[0]
        ret = create_menus(app_id, setting.APP_MENUS)
        logger.info(ret)

