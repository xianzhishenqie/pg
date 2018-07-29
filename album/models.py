from django.db import models
from django.utils import timezone

from pg_auth.models import User


class MusicTag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Music(models.Model):
    name = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    file = models.FileField(upload_to='music', default='')
    url = models.URLField()

    lyric_file = models.FileField(upload_to='lyric', default='')
    lyric_url = models.URLField(default='')

    tags = models.ManyToManyField(MusicTag)

    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)


class TemplateTag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Template(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cover = models.ImageField(upload_to='template_cover', default='')
    cover_url = models.URLField(default='')
    path_name = models.CharField(max_length=100)

    tags = models.ManyToManyField(TemplateTag)
    default_music = models.ForeignKey(Music, on_delete=models.SET_NULL, null=True, default=None)

    create_time = models.DateTimeField(default=timezone.now)


class Picture(models.Model):
    seq = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='album', default='')

    class Meta:
        ordering = ('seq',)


class Album(models.Model):
    name = models.CharField(max_length=100, default='')
    desc = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    pictures = models.ManyToManyField(Picture)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, default=None)
    music = models.ForeignKey(Music, on_delete=models.SET_NULL, null=True, default=None)

    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

