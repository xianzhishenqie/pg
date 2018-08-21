
import urllib

from django.conf import settings

from rest_framework.fields import ImageField
from rest_framework.reverse import reverse

from base.utils.enum import Enum
from base.utils.text import ec

from we import models as we_models
from we.utils.handlers import UserMessageHandler as BaseUserMessageHandler

from album.utils import common


class UserMessageHandler(BaseUserMessageHandler):

    TextRes = Enum(
        CREATE_ALBUM='创建相册',
        LIST_ALBUM='查看相册',
        MANAGE='管理',
    )

    def handle_text(self):
        content = self.content.strip()
        if content == self.TextRes.CREATE_ALBUM:
            we_user = we_models.WeUser.objects.get(openid=self.from_username)
            album = common.get_or_create_default_album(we_user.user)
            res = self.result(
                self._create_album_msg(
                    self._pic_url(we_user, album),
                    self._news_url(reverse('album:web:album_display', (album.pk,)), we_user.openid_key, query={'edit': 1}),
                )
            )
        elif content == self.TextRes.LIST_ALBUM:
            we_user = we_models.WeUser.objects.get(openid=self.from_username)
            res = self.result(
                self._list_album_msg(
                    self._pic_url(we_user),
                    self._news_url(reverse('album:web:album_list'), we_user.openid_key)
                )
            )
        elif content == self.TextRes.MANAGE:
            we_user = we_models.WeUser.objects.get(openid=self.from_username)
            if we_user.user.is_staff:
                res = self.result(
                    self._manage_msg(
                        self._news_url(reverse('album:cms:album_manage'), we_user.openid_key),
                        self._news_url(reverse('album:cms:music_manage'), we_user.openid_key),
                    )
                )
            else:
                res = ''
        else:
            res = ''

        return res

    def _create_album_msg(self, pic_url, news_url):
        return {
                'MsgType': 'news',
                'ArticleCount': 1,
                'Articles': [{
                    'Title': ec('创建相册'),
                    'Description': ec('创建我的相册'),
                    'PicUrl': pic_url,
                    'Url':  news_url,
                }],
            }

    def _list_album_msg(self, pic_url, news_url):
        return {
                'MsgType': 'news',
                'ArticleCount': 1,
                'Articles': [{
                    'Title': ec('我的相册'),
                    'Description': ec('查看我的相册'),
                    'PicUrl': pic_url,
                    'Url': news_url
                }],
            }

    def _manage_msg(self, album_url, music_url):
        return {
                'MsgType': 'news',
                'ArticleCount': 3,
                'Articles': [{
                    'Title': ec('管理'),
                    'Description': '',
                    'PicUrl': '',
                    'Url': ''
                },{
                    'Title': ec('相册管理'),
                    'Description': '',
                    'PicUrl': '',
                    'Url': album_url
                },{
                    'Title': ec('音乐管理'),
                    'Description': '',
                    'PicUrl': '',
                    'Url': music_url
                }],
            }

    def _pic_url(self, we_user, album=None):
        if not album:
            album = common.get_or_create_default_album(we_user.user)
        picture = album.pictures.first()
        if picture:
            pic_url = ImageField.to_representation(picture.image)
        else:
            pic_url = album.template.cover_url or ImageField.to_representation(album.template.cover)

        return pic_url

    def _news_url(self, path, key, query=None):
        query_params = {'key': key}
        if query:
            query_params.update(query)
        url = '{server}{path}?{query}'.format(
                  server=settings.SERVER,
                  path=path,
                  query=urllib.parse.urlencode(query_params)
              )
        return url
