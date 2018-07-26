
import functools

from base.utils.rest.request import RequestData


def api_request_data(func):
    @functools.wraps(func)
    def decorator(view, request, *args, **kwargs):
        request.query_data = RequestData(request, is_query=True)
        request.shift_data = RequestData(request, is_query=False)
        return func(view, request, *args, **kwargs)
    return decorator


def request_data(func):
    @functools.wraps(func)
    def decorator(request, *args, **kwargs):
        request.query_data = RequestData(request, is_query=True)
        request.shift_data = RequestData(request, is_query=False)
        return func(request, *args, **kwargs)
    return decorator

