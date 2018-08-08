import json

from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from base.utils import views as default_views
from base.utils.render import get_app_render
from base.utils.rest.decorators import request_data

from we.utils.decorators import auto_login

from album import models as album_models
from album.utils import common

from . import serializers as mserializers


render = get_app_render(__package__)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@request_data
@auto_login()
def album_list_page(request):
    context = {}
    return render(request, 'album_list.html', context)


@api_view(['GET'])
@permission_classes((AllowAny,))
@request_data
@auto_login(ignore=True)
def album_display_page(request, pk):
    has_key = False
    openid_key = request.query_params.get('key')
    if openid_key and request.user.is_authenticated and openid_key == request.user.weuser.openid_key:
        has_key = True

    if pk == 0 and request.user.is_authenticated:
        album = common.get_or_create_default_album(request.user)
    else:
        try:
            album = album_models.Album.objects.get(pk=pk)
        except Exception as e:
            return default_views.Http404Page(request, e)

    album_data = mserializers.AlbumSerializers(album).data
    picture_images = [picture_data['image'] for picture_data in album_data['picture_list']]

    context = {
        'pk': album.pk,
        'has_key': has_key,
        'is_owner': album.user == request.user,
        'album': album,
        'album_data': album_data,
        'pictures': json.dumps(picture_images),
        'share_img': picture_images[0] if len(picture_images) > 0 else '',
    }

    return render(request, 'album_display.html', context)

#
# @api_view(['GET', 'POST'])
# @permission_classes((IsAuthenticated,))
# @request_data
# def crawl(request):
#     if request.method == 'GET':
#         return render(request, 'crawl.html')
#     else:
#         import os
#         import requests
#         from pyquery import PyQuery as pq
#         from rest_framework.response import Response
#         from base.utils.thread import delay_exe
#         def download_img(url):
#             paths = url.split('/')
#             base_dir = os.path.join(settings.BASE_DIR, 'album/static/album/web/img/album_template', paths[-2])
#             if not os.path.exists(base_dir):
#                 try:
#                     os.makedirs(base_dir)
#                 except:
#                     pass
#             filepath = os.path.join(base_dir, paths[-1])
#             res = requests.get(url)
#             with open(filepath, 'wb') as f:
#                 f.write(res.content)
#
#         url = request.shift_data.get('url')
#         doc = pq(url)
#         imgs = doc('img[src^="http://wangjianxun1.test.upcdn.net/img/album_template/"]')
#         srcs = set()
#         for img in imgs.items():
#             srcs.add(img.attr.src)
#
#         for src in srcs:
#             delay_exe(download_img, 0, (src,))
#
#         return Response(list(srcs))




