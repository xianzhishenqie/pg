
import hashlib

from django.conf import settings


def ec(t):
    return t.encode(settings.ENCODING)


def dc(t):
    return t.decode(settings.ENCODING)


def md5(t):
    return hashlib.md5(ec(t)).hexdigest()


def sha1(t):
    return hashlib.sha1(ec(t)).hexdigest()