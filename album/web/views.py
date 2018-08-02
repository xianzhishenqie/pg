import urllib

from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse

from base.utils import views as default_views
from base.utils.render import get_app_render
from base.utils.rest.decorators import request_data

from we import setting as we_setting
from we.utils.decorators import auto_login

from album.utils import common


render = get_app_render(__package__)


@api_view(['GET'])
@permission_classes([AllowAny])
@request_data
def index(request):
    context = {}
    redirect_uri = '{server}{url}'.format(server=settings.SERVER, url=reverse('we:web:code'))
    context['code_url'] = we_setting.SILENT_CODE_URL.format(redirect_uri=urllib.request.quote(redirect_uri))

    return render(request, 'index.html', context)



@api_view(['GET'])
@permission_classes([AllowAny])
@request_data
@auto_login
def album_page(request, pk):
    if pk == 0:
        try:
            album = common.get_or_create_default_album(request.user)
        except Exception as e:
            return default_views.Http404Page()
        pk = album.pk

    context = {
        'pk': pk,
    }

    return render(request, 'album.html', context)


@api_view(['GET'])
@permission_classes([AllowAny])
@request_data
@auto_login
def album_list_page(request):
    context = {}
    return render(request, 'album_list.html', context)


@api_view(['GET'])
@permission_classes([AllowAny])
@request_data
@auto_login
def album_display_page(request, pk):
    context = {
        'pk': pk,
    }

    return render(request, 'album_display.html', context)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@request_data
def crawl(request):
    if request.method == 'GET':
        return render(request, 'crawl.html')
    else:
        import os
        import requests
        from pyquery import PyQuery as pq
        from rest_framework.response import Response
        from base.utils.thread import delay_exe
        def download_img(url):
            paths = url.split('/')
            base_dir = os.path.join(settings.BASE_DIR, 'album/static/album/web/img/album_template', paths[-2])
            if not os.path.exists(base_dir):
                try:
                    os.makedirs(base_dir)
                except:
                    pass
            filepath = os.path.join(base_dir, paths[-1])
            res = requests.get(url)
            with open(filepath, 'wb') as f:
                f.write(res.content)

        url = request.shift_data.get('url')
        doc = pq(url)
        imgs = doc('img[src^="http://wangjianxun1.test.upcdn.net/img/album_template/"]')
        srcs = set()
        for img in imgs.items():
            srcs.add(img.attr.src)

        for src in srcs:
            delay_exe(download_img, 0, (src,))

        return Response(list(srcs))




