# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common_framework.utils.rest.request import RequestData
from common_framework.utils.x_logger import get_x_logger

logger = get_x_logger(__name__)


class RequestDataMixin(object):
    def initial(self, request, *args, **kwargs):
        super(RequestDataMixin, self).initial(request, *args, **kwargs)
        self.query_data = RequestData(request, is_query=True)
        self.shift_data = RequestData(request, is_query=False)
