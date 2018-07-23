
from base.utils.rest.request import RequestData


def request_data(func):
    def decorator(request, *args, **kwargs):
        request.query_data = RequestData(request, is_query=True)
        request.shift_data = RequestData(request, is_query=False)
        return func(request, *args, **kwargs)
    return decorator