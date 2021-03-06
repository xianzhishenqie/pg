
import logging

from base.utils.http import HttpClient

from we import setting
from we.utils import common


logger = logging.getLogger(__name__)


def create_menus(app_id, menus):
    access_token = common.get_access_token(app_id)
    app_menu_create_url = setting.APPS[app_id]['APP_MENU_CREATE_URL']
    http = HttpClient()
    ret = http.jpost(app_menu_create_url.format(access_token=access_token), data=menus)
    return ret