import hashlib

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from base.utils.http import HttpClient
from base.utils.rest.decorators import request_data
from base.utils.text import ec

from we import setting


@api_view(['GET'])
@permission_classes([AllowAny])
@request_data
def we_access(request):
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


@api_view(['GET'])
@request_data
def we_code(request):
    code = request.query_data.get('code')

    http = HttpClient()
    res = http.mget(setting.ACCESS_TOKEN_URL.format(code=code))
    ret = http.result(res, json=True)

    access_token = ret['access_token']

    return Response(ret)
