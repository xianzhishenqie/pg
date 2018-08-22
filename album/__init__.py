from base.utils.app import load_app_settings
from we.utils.setting import add_app as add_we_app

app_settings = load_app_settings(__package__)


def sync_app_settings():
    for app_id, app_config in app_settings.APPS.items():
        add_we_app(app_id, app_config)