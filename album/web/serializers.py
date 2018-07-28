from rest_framework import serializers


from album import models as album_models



class MusicTagSerializers(serializers.ModelSerializer):

    class Meta:
        model = album_models.MusicTag
        fields = ('id', 'name')


class MusicSerializers(serializers.ModelSerializer):

    class Meta:
        model = album_models.Music
        fields = ('id', 'name', 'author', 'file', )



class PictureSerializers(serializers.ModelSerializer):

    class Meta:
        model = album_models.Picture
        fields = ('id', 'seq', 'image')


class AlbumSerializers(serializers.ModelSerializer):
    picture_list = serializers.SerializerMethodField()

    def get_picture_list(self, obj):
        return PictureSerializers(obj.pictures.all(), many=True).data

    class Meta:
        model = album_models.Album
        fields = ('id', 'name', 'user', 'picture_list')
        read_only_fields = ('type', 'name', 'user')