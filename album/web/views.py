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