
from django.db import transaction

from rest_framework import exceptions, filters, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from base.utils.models.data import get_sub_model_data
from base.utils.rest import mixins as common_mixins
from base.utils.rest.decorators import api_request_data

from album import models as album_models

from . import serializers as mserializers


class MusicTagViewSet(common_mixins.PGMixin,
                      viewsets.ReadOnlyModelViewSet):
    queryset = album_models.MusicTag.objects.all()
    serializer_class = mserializers.MusicTagSerializers
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering_fields = ('id',)
    ordering = ('id',)


class MusicViewSet(common_mixins.PGMixin,
                   viewsets.ReadOnlyModelViewSet):
    queryset = album_models.Music.objects.all()
    serializer_class = mserializers.MusicSerializers
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'author')

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

