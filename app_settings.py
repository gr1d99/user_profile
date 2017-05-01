# for future use
class AppSettings(object):

    def __init__(self, prefix):
        self.prefix = prefix
        self.required_apps = [
            'betterforms',
            'braces',
            'crispy_forms',
            'phonenumber_field',
        ]

    def _setting(self, name, dflt):
        from django.conf import settings
        getter = getattr(settings,
                         'USERPROFILE_SETTING_GETTER',
                         lambda name, dflt: getattr(settings, name, dflt))
        return getter(self.prefix + name, dflt)

    @property
    def INSTALLED_APPS(self):
        from django.conf import settings
        return self._setting("INSTALLED_APPS",
                             getattr(settings, "INSTALLED_APPS"))

import sys
app_settings = AppSettings('USERPROFILE_')
app_settings.__name__ = __name__
sys.modules[__name__] = app_settings


