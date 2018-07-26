
from django.db import transaction

from rest_framework import exceptions, filters, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from base.utils.models.data import get_sub_model_data
from base.utils.rest import mixins as common_mixins
from base.utils.rest.decorators import api_request_data

from album import models as album_models

from . import serializers as mserializers


class AlbumViewSet(common_mixins.RequestDataMixin,
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

        user = self.query_data.get('user')
        if user is not None:
            queryset = queryset.filter(user__username=user)
        else:
            raise exceptions.PermissionDenied()

        return queryset

    def perform_destroy(self, instance):
        for picture in instance.pictures.all():
            picture.image.delete()
            picture.delete()
        instance.delete()

    @action(['POST'], detail=True)
    @api_request_data
    def picture(self, request, pk=None):
        if pk == 0:
            instance = album_models.Album.objects.create(
                user=request.user,
            )
        else:
            instance = self.get_object()

        picture_data = get_sub_model_data(request.data, 'picture')
        picture_serializer = mserializers.PictureSerializers(picture_data)
        picture_serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            picture_serializer.save()
            instance.pictures.add(picture_serializer.instance)
        return Response(picture_serializer.data)
