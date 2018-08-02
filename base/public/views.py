# -*- coding: utf-8 -*-

from django.conf import settings
from django.views.static import serve

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def media(request, path):
    return serve(request, path, document_root=settings.MEDIA_ROOT)

