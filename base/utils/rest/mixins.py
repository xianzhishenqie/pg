# -*- coding: utf-8 -*-
from base.utils.rest.request import RequestData


class RequestDataMixin(object):
    def initial(self, request, *args, **kwargs):
        super(RequestDataMixin, self).initial(request, *args, **kwargs)
        self.query_data = RequestData(request, is_query=True)
        self.shift_data = RequestData(request, is_query=False)
