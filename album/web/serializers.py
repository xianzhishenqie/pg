import os
from rest_framework import serializers

from base.utils.text import rk_filename

from album import models as album_models
from album.utils import common


class TemplateTagSerializers(serializers.ModelSerializer):

    class Meta:
        model = album_models.TemplateTag
        fields = ('id', 'name')


class TemplateSerializers(serializers.ModelSerializer):

    def to_internal_value(self, data):
        cover = data.get('cover')
        if cover:
            cover.name = rk_filename(cover.name)

        return super(TemplateSerializers, self).to_internal_value(data)

    class Meta:
        model = album_models.Template
        fields = ('id', 'name', 'cover', 'cover_url')


class MusicTagSerializers(serializers.ModelSerializer):

    class Meta:
        model = album_models.MusicTag
        fields = ('id', 'name')


class MusicSerializers(serializers.ModelSerializer):

    def to_internal_value(self, data):
        file = data.get('file')
        if file:
            file.name = rk_filename(file.name)

        lyric_file = data.get('lyric_file')
        if lyric_file:
            lyric_file.name = rk_filename(lyric_file.name)

        return super(MusicSerializers, self).to_internal_value(data)

    class Meta:
        model = album_models.Music
        fields = ('id', 'name', 'author', 'file', 'url')



class PictureSerializers(serializers.ModelSerializer):

    def to_internal_value(self, data):
        image = data.get('image')
        if image:
            image.name = rk_filename(image.name)

        return super(PictureSerializers, self).to_internal_value(data)

    class Meta:
        model = album_models.Picture
        fields = ('id', 'seq', 'image')


class AlbumSerializers(serializers.ModelSerializer):
    picture_list = serializers.SerializerMethodField()

    music_data = serializers.SerializerMethodField()

    template_data = serializers.SerializerMethodField()

    def get_picture_list(self, obj):
        return PictureSerializers(obj.pictures.all(), many=True).data

    def get_music_data(self, obj):
        if obj.music:
            return MusicSerializers(obj.music).data
        else:
            return None

    def get_template_data(self, obj):
        if not obj.template:
            common.fix_empty_template_album(obj)

        if obj.template:
            return TemplateSerializers(obj.template).data
        else:
            return None

    def update(self, instance, validated_data):
        if not validated_data.get('music') and validated_data.get('template'):
            template = validated_data.get('template')
            validated_data['music'] = template.default_music

        return super(AlbumSerializers, self).update(instance, validated_data)

    class Meta:
        model = album_models.Album
        fields = ('id', 'name', 'desc', 'user', 'music', 'template', 'picture_list', 'music_data', 'template_data')
        read_only_fields = ('user',)