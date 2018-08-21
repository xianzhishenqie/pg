import logging
import os

from django.conf import settings
from django.core.management import BaseCommand


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('p', nargs='+', type=str)

    def handle(self, *args, **options):
        path_name = options.get('p')[0]
        base_dir = os.path.join(settings.BASE_DIR, 'album/static/album/web/img/album_template', path_name)
        for filename in os.listdir(base_dir):
            print('''<img class="animated bounce" src="{{% static 'album/web/img/album_template/{}/{}' %}}">'''.format(path_name, filename))


