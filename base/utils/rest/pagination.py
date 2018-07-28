# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict

from rest_framework import pagination, response


class BootstrapPagination(pagination.LimitOffsetPagination):
    max_limit = 1000

    def get_paginated_response(self, data):
        return response.Response(OrderedDict([
            ('total', self.count),
            ('rows', data)
        ]))