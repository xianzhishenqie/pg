
from django.contrib.auth.models import AbstractUser
from django.db import models

from base.utils.enum import Enum


class User(AbstractUser):
    logo = models.ImageField(upload_to='user_logo', default='')
    nickname = models.CharField(max_length=100, default='')

    Status = Enum(
        DELETE=0,
        NORMAL=1,
    )
    status = models.PositiveIntegerField(default=Status.NORMAL)

    extra = models.TextField(default='')
