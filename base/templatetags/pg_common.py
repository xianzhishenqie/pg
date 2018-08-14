# -*- coding: utf-8 -*-
import os

from django import template
from django.conf import settings
from django.templatetags.static import StaticNode

from base.utils.text import md5

register = template.Library()


class StaticVNode(StaticNode):

    def render(self, context):
        url = self.url(context)
        if self.varname is None:
            return get_url_with_version(url)
        context[self.varname] = url
        return ''


@register.tag('static_v')
def do_static_v(parser, token):
    return StaticVNode.handle_token(parser, token)


def static_v(path):
    return StaticVNode.handle_simple(path)

def get_url_with_version(url):
    for vdir in settings.STATIC_V_DIRS:
        file_path = os.path.join(vdir, url.lstrip('/'))
        if os.path.exists(file_path):
            modified_time = os.path.getmtime(file_path)
            modified_time = md5(str(modified_time))
            return '%s?%s' % (url, modified_time)
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
