
# 实际
APP_ID = 'wxa1a56bc0b9597354'

APP_SECRET = 'da513aacaa2f127e5a1dc2e4246a20e9'

# 测试
# APP_ID = 'wx6f6efb9359dd6759'
#
# APP_SECRET = 'e6536f2b3a614f7cba0236c0fec23069'

TOKEN = '920425'

APP_ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (APP_ID, APP_SECRET)

APP_MENU_CREATE_URL = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={access_token}'


SILENT_CODE_URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri={redirect_uri}&response_type=code&scope=snsapi_base&state=123#wechat_redirect' % APP_ID

ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code={code}&grant_type=authorization_code' % (APP_ID, APP_SECRET)

USER_MESSAGE_HANDLER = 'album.utils.handlers.UserMessageHandler'