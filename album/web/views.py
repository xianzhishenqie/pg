

from base.utils.render import get_app_render

render = get_app_render(__package__)


def index(request):
    return render(request, 'index.html')