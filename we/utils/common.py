
import datetime

from django.utils import timezone

from base.utils.http import HttpClient

from we import setting
from we.models import WeAppInfo


def get_access_token():
    app_info = WeAppInfo.objects.first()
    if not _valid_access_token(app_info):
        ret = pull_access_token()
        access_token = ret['access_token']
        expires_in = ret['expires_in']
        expire_time = timezone.now() + datetime.timedelta(seconds=expires_in)
        if not app_info:
            app_info = WeAppInfo()
        app_info.access_token = access_token
        app_info.access_token_expire_time = expire_time
        app_info.save()

    return app_info.access_token


def _valid_access_token(app_info):
    if not app_info:
        return False

    if app_info.access_token_expire_time <= timezone.now():
        return False

    return True


def pull_access_token():
    http = HttpClient()
    ret = http.jget(setting.APP_ACCESS_TOKEN_URL)
    return ret