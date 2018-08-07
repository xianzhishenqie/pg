from django.utils.module_loading import import_string
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes, parser_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response

from base.utils.http import HttpClient
from base.utils.rest.decorators import request_data
from base.utils.rest.parsers import TextXMLParser

from we import setting
from we.utils import common
from we.utils.handlers import UserMessageHandler
from we.utils.rest.renderers import CDATATextXMLRenderer


@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
@parser_classes((TextXMLParser,))
@renderer_classes((CDATATextXMLRenderer, StaticHTMLRenderer))
@csrf_exempt
@request_data
def we_access(request):
    signature = request.query_data.get('signature')
    timestamp = request.query_data.get('timestamp')
    nonce = request.query_data.get('nonce')
    echostr = request.query_data.get('echostr')

    if request.method == 'GET':
        if not common.is_we_access(signature, timestamp, nonce):
            echostr = ''

        return Response(echostr)
    elif request.method == 'POST':
        if not common.is_we_access(signature, timestamp, nonce):
            return Response(echostr)

        openid = request.query_data.get('openid')
        common.sync_openid(openid)

        handler = import_string(setting.USER_MESSAGE_HANDLER)(request.shift_data)
        echostr = handler.handle()

        return Response(echostr)


@api_view(['GET'])
@request_data
def we_code(request):
    code = request.query_data.get('code')

    http = HttpClient()
    ret = http.jget(setting.ACCESS_TOKEN_URL.format(code=code))
    access_token = ret['access_token']

    return Response(ret)

