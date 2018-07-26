from rest_framework import serializers


from album import models as album_models




class PictureSerializers(serializers.ModelSerializer):

    class Meta:
        model = album_models.Album
        fields = ('id', 'seq', 'image')


class AlbumSerializers(serializers.ModelSerializer):
    picture_list = serializers.SerializerMethodField()

    def get_picture_list(self, obj):
        return [picture.image.url for picture in obj.pictures.all()]

    class Meta:
        model = album_models.Album
        fields = ('id', 'name', 'user')
        read_only_fields = ('type', 'name', 'user')