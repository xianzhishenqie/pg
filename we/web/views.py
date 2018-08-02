import hashlib

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response

from base.utils.http import HttpClient
from base.utils.rest.decorators import request_data
from base.utils.text import ec

from we import setting
from we.utils import common


@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
@renderer_classes((StaticHTMLRenderer,))
@csrf_exempt
@request_data
def we_access(request):
    if request.method == 'GET':
        signature = request.query_data.get('signature')
        timestamp = request.query_data.get('timestamp')
        nonce = request.query_data.get('nonce')
        echostr = request.query_data.get('echostr')

        try:
            signature_list = sorted([setting.TOKEN, timestamp, nonce])
            calc_signature = hashlib.sha1(ec(''.join(signature_list))).hexdigest()
        except:
            pass
        else:
            if calc_signature != signature:
                echostr = None

        return Response(echostr)
    elif request.method == 'POST':
        openid = request.query_data.get('openid')
        common.sync_openid(openid)
        return Response()


@api_view(['GET'])
@request_data
def we_code(request):
    code = request.query_data.get('code')

    http = HttpClient()
    ret = http.jget(setting.ACCESS_TOKEN_URL.format(code=code))
    access_token = ret['access_token']

    return Response(ret)


@api_view(['GET'])
@request_data
def we_event(request):
    code = request.query_data.get('code')
    return Response({})
