from __future__ import absolute_import, division, print_function, unicode_literals

from django.apps import AppConfig


class GargoyleAppConfig(AppConfig):
    name = 'gargoyle'
    verbose_name = 'Gargoyle'

    def ready(self):
        from gargoyle.checks import check_default_switch_status
        self.module.autodiscover()
