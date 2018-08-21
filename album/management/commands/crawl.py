import logging
import os
import requests

from pyquery import PyQuery as pq

from django.conf import settings
from django.core.management import BaseCommand


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'http://photo.91youxing.com/index.php?g=Wap&m=Photo&a=index&token=nbozvy1523608960&bookname=oWKJOuD1sni87WtOJ5x88pLW31hgwqlcms1531403344'
        doc = pq(url)
        imgs = doc('img[src^="http://wangjianxun1.test.upcdn.net/img/album_template/"]')
        for img in imgs.items():
            download_img(img.attr.src)


def download_img(url):
    paths = url.split('/')
    base_dir = os.path.join(settings.BASE_DIR, 'album/static/album/web/img/album_template', paths[-2])
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    filepath = os.path.join(base_dir, paths[-1])
    res = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(res.content)

