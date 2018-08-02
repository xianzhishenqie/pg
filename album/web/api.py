
from django.db import transaction
from django.db.models import Count

from rest_framework import exceptions, filters, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from base.utils.models.data import get_sub_model_data
from base.utils.rest import mixins as common_mixins
from base.utils.rest.decorators import api_request_data

from album import models as album_models

from . import serializers as mserializers



class TemplateTagViewSet(common_mixins.CacheModelMixin,
                         common_mixins.PGMixin,
                         viewsets.ReadOnlyModelViewSet):
    queryset = album_models.TemplateTag.objects.all()
    serializer_class = mserializers.TemplateTagSerializers
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id',)
    ordering = ('id',)

    page_cache_age = None
    unlimit_pagination = True


class TemplateViewSet(common_mixins.CacheModelMixin,
                      common_mixins.PGMixin,
                      viewsets.ReadOnlyModelViewSet):
    queryset = album_models.Template.objects.filter(public=True)
    serializer_class = mserializers.TemplateSerializers
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)

    ordering_fields = ('create_time',)
    ordering = ('-create_time',)

    page_cache_age = None
    unlimit_pagination = True

    def get_queryset(self):
        queryset = self.queryset

        tag = self.query_data.get('tag', int)
        if tag:
            if tag == -1:
                queryset = queryset.annotate(album_count=Count('album')).order_by('-album_count')
            elif tag == -2:
                pass
            else:
                queryset = queryset.filter(tags=tag)

        return queryset


class MusicTagViewSet(common_mixins.CacheModelMixin,
                      common_mixins.PGMixin,
                      viewsets.ReadOnlyModelViewSet):
    queryset = album_models.MusicTag.objects.all()
    serializer_class = mserializers.MusicTagSerializers
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id',)
    ordering = ('id',)

    page_cache_age = None
    unlimit_pagination = True


class MusicViewSet(common_mixins.CacheModelMixin,
                   common_mixins.PGMixin,
                   viewsets.ReadOnlyModelViewSet):
    queryset = album_models.Music.objects.all()
    serializer_class = mserializers.MusicSerializers
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'author')

    page_cache_age = None
    unlimit_pagination = True

    def get_queryset(self):
        queryset = self.queryset

        tag = self.query_data.get('tag', int)
        if tag:
            queryset = queryset.filter(tags=tag)

        return queryset


class AlbumViewSet(common_mixins.PGMixin,
                   viewsets.ModelViewSet):
    queryset = album_models.Album.objects.all()
    serializer_class = mserializers.AlbumSerializers
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('-create_time',)
    ordering = ('-create_time',)

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_destroy(self, instance):
        for picture in instance.pictures.all():
            picture.image.delete()
            picture.delete()
        instance.delete()

    @action(['POST', 'DELETE'], detail=True)
    @api_request_data
    def picture(self, request, pk=None):
        if request.method == 'POST':
            instance = self.get_object()

            picture_data = get_sub_model_data(request.data, ['picture'])
            picture_serializer = mserializers.PictureSerializers(data=picture_data)
            picture_serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                if not instance.pk:
                    instance.save()
                picture_serializer.save()
                instance.pictures.add(picture_serializer.instance)
            return Response(picture_serializer.data)
        elif request.method == 'DELETE':
            instance = self.get_object()
            picture_data = get_sub_model_data(request.data, ['picture'])
            picture_id = picture_data.get('id')
            if picture_id:
                instance.pictures.filter(pk=picture_id).delete()
            else:
                raise exceptions.NotFound()

            return Response(status=status.HTTP_204_NO_CONTENT)

