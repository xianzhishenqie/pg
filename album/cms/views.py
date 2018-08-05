import json
import urllib

from django.conf import settings

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.reverse import reverse

from base.utils import views as default_views
from base.utils.render import get_app_render
from base.utils.rest.decorators import request_data

from we import setting as we_setting
from we.utils.decorators import auto_login

from album import models as album_models
from album.utils import common

from . import serializers as mserializers


render = get_app_render(__package__)


@api_view(['GET'])
@permission_classes([IsAdminUser])
@request_data
@auto_login()
def music_manage_page(request):
    context = {}
    return render(request, 'music_manage.html', context)





