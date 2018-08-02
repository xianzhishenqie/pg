
import functools

from django.contrib.auth import login

from base.utils import views as default_views

from we import models as we_models


def auto_login(func):
    @functools.wraps(func)
    def decorator(request, *args, **kwargs):
        if not request.user.is_authenticated:
            openid_key = request.GET.get('key')
            if not openid_key:
                return default_views.Http403Page(request)

            we_user = we_models.WeUser.objects.filter(openid_key=openid_key).first()
            if not we_user:
                return default_views.Http403Page(request)

            login(request, we_user.user)

        return func(request, *args, **kwargs)
    return decorator
