from django.db import models


class WeUser(models.Model):
    openid = models.CharField(max_length=100)