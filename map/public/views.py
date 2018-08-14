import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from base.utils.render import get_app_render
from base.utils.rest.decorators import request_data




render = get_app_render(__package__)



@api_view(['GET'])
@permission_classes((AllowAny,))
@request_data
def test_page(request):
    context = {}
    return render(request, 'test.html', context)

