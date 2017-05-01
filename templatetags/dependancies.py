from django import template

from .. import app_settings


register = template.Library()


class RequirementsNode(template.Node):
    def __init__(self, context_name):
        self.context_name = context_name

    def render(self, context):
        required_apps = app_settings.required_apps
        installed_apps = app_settings.INSTALLED_APPS

        missing_apps = []

        for app in required_apps:
            if app not in installed_apps:
                missing_apps.append(app)

        error_message = ("it appears `%s` are not in your `settings.py` INSTALLED_APPS"
                         % ', '.join(missing_apps))
        if len(missing_apps) > 0:
            raise template.TemplateSyntaxError(error_message)

        return ''


@register.tag
def check_requirements(parser, token):
    bits = token.split_contents()
    error_message = ("%(tag_name)s tag does not expect any arguments" % dict(tag_name=bits[0]))
    if not len(bits) > 1:
        context_name = bits[-1]
        return RequirementsNode(context_name)

    else:
        raise template.TemplateSyntaxError(
            error_message
        )

