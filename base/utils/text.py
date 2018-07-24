
from django.conf import settings


def ec(t):
    return t.encode(settings.ENCODING)