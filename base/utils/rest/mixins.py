# -*- coding: utf-8 -*-
from base.utils.rest.pagination import BootstrapPagination
from base.utils.rest.request import RequestData


class PGMixin(object):

    pagination_class = BootstrapPagination

    def initial(self, request, *args, **kwargs):
        super(PGMixin, self).initial(request, *args, **kwargs)
        self.query_data = RequestData(request, is_query=True)
        self.shift_data = RequestData(request, is_query=False)
