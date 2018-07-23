

APP_ID = 'wxa1a56bc0b9597354'

APP_SECRET = 'da513aacaa2f127e5a1dc2e4246a20e9'

SILENT_CODE_URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri={redirect_uri}&response_type=code&scope=snsapi_base&state=1#wechat_redirect' % APP_ID

ACCESS_TOKEN_URL= 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code={code}&grant_type=authorization_code' % (APP_ID, APP_SECRET)