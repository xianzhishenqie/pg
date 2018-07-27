
import logging

from base.utils.http import HttpClient

from we import setting
from we.utils import common


logger = logging.getLogger(__name__)


def create_menus(menus):
    access_token = common.get_access_token()
    http = HttpClient()
    ret = http.jpost(setting.APP_MENU_CREATE_URL.format(access_token=access_token), data=menus)
    return ret