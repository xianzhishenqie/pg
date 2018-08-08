from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

from base.utils.render import get_app_render
from base.utils.rest.decorators import request_data

from we.utils.decorators import auto_login


render = get_app_render(__package__)


@api_view(['GET'])
@permission_classes((IsAdminUser,))
@request_data
@auto_login()
def album_manage_page(request):
    context = {}
    return render(request, 'album_manage.html', context)



@api_view(['GET'])
@permission_classes((IsAdminUser,))
@request_data
@auto_login()
def music_manage_page(request):
    context = {}
    return render(request, 'music_manage.html', context)





