import os

from django import template
from django.conf import settings
from django.templatetags.static import StaticNode
from django.utils.html import conditional_escape

from base.utils.text import md5

register = template.Library()


class PGStaticNode(StaticNode):

    def render(self, context):
        url = self.url(context)
        if context.autoescape:
            url = conditional_escape(url)
        url = get_resource_url(url)
        if self.varname is None:
            return url
        context[self.varname] = url
        return ''


class PGStaticVNode(StaticNode):

    def render(self, context):
        url = self.url(context)
        if context.autoescape:
            url = conditional_escape(url)
        url = get_resource_url(get_url_with_version(url))
        if self.varname is None:
            return url
        context[self.varname] = url
        return ''


@register.tag('pg_static')
def do_static_v(parser, token):
    return PGStaticNode.handle_token(parser, token)


@register.tag('pg_static_v')
def do_static_v(parser, token):
    return PGStaticVNode.handle_token(parser, token)


def get_url_with_version(url):
    app_name = url.split('/')[2]
    v_dir = settings.STATIC_V_DIRS[app_name]
    file_path = os.path.join(v_dir, url.lstrip('/'))
    if os.path.exists(file_path):
        modified_time = os.path.getmtime(file_path)
        modified_time = md5(str(modified_time))
        return '%s?%s' % (url, modified_time)
    return url


def get_resource_url(url):
    if settings.RESOURCE_SERVER:
        return '{}{}'.format(settings.RESOURCE_SERVER, url)
    return url


class SettingsNode(template.Node):
    def __init__(self, variable):
        self.variable = variable

    def render(self, context):
        context[self.variable] = settings
        return ''


@register.tag("get_settings")
def do_get_settings(parser, token):
    args = token.contents.split()
    if len(args) != 3 or args[1] != 'as':
        raise template.TemplateSyntaxError("'get_settings' requires 'as variable' (got %r)" % args)

    return SettingsNode(args[2])
