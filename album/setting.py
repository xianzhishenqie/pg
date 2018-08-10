from we.setting import add_app as add_we_app


APPS = {
    'wxa1a56bc0b9597354': {
        'APP_SECRET': '',
        'TOKEN': '920425',
        'USER_MESSAGE_HANDLER': 'album.utils.handlers.UserMessageHandler',
    },
    'wx6f6efb9359dd6759': {
        'APP_SECRET': 'e6536f2b3a614f7cba0236c0fec23069',
        'TOKEN': '920425',
        'USER_MESSAGE_HANDLER': 'album.utils.handlers.UserMessageHandler',
    }
}
for app_id, app_config in APPS.items():
    add_we_app(app_id, app_config)



ALBUM_PICTURE_LIMIT = 8

APP_MENUS = {
    "button": [{
        "type": "click",
        "name": "我的相册",
        "key": "MY_ALBUM",
        "url": "",
    }]
}


