from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.utils.http import HttpClient
from base.utils.rest.decorators import request_data

from we import setting


@api_view(['GET'])
@request_data
def we_code(request):
    code = request.query_data.get('code')

    http = HttpClient()
    res = http.mget(setting.ACCESS_TOKEN_URL.format(code=code))
    ret = http.result(res, json=True)

    access_token = ret['access_token']

    return Response(ret)
