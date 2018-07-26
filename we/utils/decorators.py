
import functools

from django.contrib.auth import login

from base.utils import views as default_views

from we import models as we_models


def auto_login(func):
    @functools.wraps(func)
    def decorator(request, *args, **kwargs):
        if not request.user.is_authenticated:
            openid = request.GET.get('user')
            if not openid:
                return default_views.Http403Page(request)

            we_user = we_models.WeUser.objects.filter(openid=openid).first()
            if not we_user:
                return default_views.Http403Page(request)

            login(request, we_user.user)

        return func(request, *args, **kwargs)
    return decorator
