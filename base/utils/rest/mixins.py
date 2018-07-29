# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models.sql.datastructures import EmptyResultSet
from django.utils import six
from django.utils.module_loading import import_string

from base.utils.cache import CacheProduct, delete_cache
from base.utils.text import md5
from base.utils.rest.pagination import BootstrapPagination, CacheBootstrapPagination
from base.utils.rest.request import RequestData


class PGMixin(object):

    pagination_class = BootstrapPagination

    def initial(self, request, *args, **kwargs):
        super(PGMixin, self).initial(request, *args, **kwargs)
        self.query_data = RequestData(request, is_query=True)
        self.shift_data = RequestData(request, is_query=False)


def _generate_cache_key(view, queryset):
    view_name = view.__class__.__name__
    try:
        key_str = queryset.query.__str__()
    except EmptyResultSet as e:
        # 无查询的空对象
        key_str = 'EmptyResultSet'

    cache_key_prefix = view.get_cache_key_prefix()
    if cache_key_prefix is not None:
        key_str = '%s:%s' % (cache_key_prefix, key_str)

    return md5('%s:%s' % (view_name, key_str))


def _generate_cache_view_name(view_cls):
    return "%s-%s" % (view_cls.__module__, view_cls.__name__)


class CacheModelMixin(object):
    pagination_class = CacheBootstrapPagination
    page_cache = True

    def __new__(cls, *args, **kwargs):
        obj = super(CacheModelMixin, cls).__new__(cls)
        view_name = _generate_cache_view_name(cls)
        obj.cache = CacheProduct(view_name)

        return obj

    def _default_generate_cache_key(self):
        return _generate_cache_key(self, self.paginator.page_queryset)

    def _default_generate_count_cache_key(self):
        return _generate_cache_key(self, self.paginator.queryset)

    def get_cache_key_prefix(self):
        return None

    def get_cache_flag(self):
        return getattr(self, 'page_cache', False)

    def get_cache_key(self):
        if not hasattr(self, 'generate_cache_key'):
            return self._default_generate_cache_key()
        return self.generate_cache_key()

    def get_cache_age(self):
        return getattr(self, 'page_cache_age', settings.DEFAULT_CACHE_AGE)

    def clear_cache(self):
        delete_cache(self.cache)
        if hasattr(self, 'related_cache_class'):
            self.clear_cls_cache(self.related_cache_class)

    @classmethod
    def clear_self_cache(cls):
        cls.clear_cls_cache(cls)

    @staticmethod
    def clear_cls_cache(cls):
        if not isinstance(cls, (list, tuple)):
            cls = [cls]
        for c in cls:
            if isinstance(c, (six.string_types, six.text_type)):
                try:
                    c = import_string(c)
                except:
                    continue
            cache_view_name = _generate_cache_view_name(c)
            cache = CacheProduct(cache_view_name)
            delete_cache(cache)

    def paginate_queryset_flag(self, queryset):
        return self.paginator.paginate_queryset_flag(queryset, self.request, view=self)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        paginate_queryset_flag = self.paginate_queryset_flag(queryset)
        if paginate_queryset_flag:
            if self.get_cache_flag():
                cache_value = self.cache.get(self.cache_key)
                if cache_value:
                    data = cache_value
                else:
                    data = self._get_list_data(queryset)
                    self.cache.set(self.cache_key, data, self.get_cache_age())
            else:
                data = self._get_list_data(queryset)
        else:
            data = []
        return self.get_paginated_response(data)

    def _get_list_data(self, queryset):
        page = self.paginate_queryset(queryset)
        data = self.get_serializer(page, many=True).data
        data = self.extra_handle_list_data(data)
        return data

    def extra_handle_list_data(self, data):
        return data

    def perform_create(self, serializer):
        if self.sub_perform_create(serializer):
            self.clear_cache()

    def perform_update(self, serializer):
        if self.sub_perform_update(serializer):
            self.clear_cache()

    def perform_destroy(self, instance):
        if self.sub_perform_destroy(instance):
            self.clear_cache()

    def sub_perform_create(self, serializer):
        super(CacheModelMixin, self).perform_create(serializer)
        return True

    def sub_perform_update(self, serializer):
        super(CacheModelMixin, self).perform_update(serializer)
        return True

    def sub_perform_destroy(self, instance):
        super(CacheModelMixin, self).perform_destroy(instance)
        return True
