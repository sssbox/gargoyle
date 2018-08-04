from __future__ import absolute_import, division, print_function, unicode_literals

from django.core.checks import Warning
from django.test import SimpleTestCase
from django.test.utils import override_settings

from gargoyle.checks import check_switch_defaults
from gargoyle.constants import GLOBAL


class CheckSwitchDefaultsTests(SimpleTestCase):
    def test_empty_fine(self):
        with override_settings(GARGOYLE_SWITCH_DEFAULTS={}):
            errors = check_switch_defaults([])
        assert errors == []

    def test_is_active_and_initial_status_present_bad(self):
        defaults = {
            'foo': {
                'is_active': True,
                'initial_status': GLOBAL,
            },
        }
        with override_settings(GARGOYLE_SWITCH_DEFAULTS=defaults):
            errors = check_switch_defaults([])
        assert errors == [
            Warning(
                '"is_active" will take precedence over "initial_status" in GARGOYLE_SWITCH_DEFAULTS.',
                hint="settings.GARGOYLE_SWITCH_DEFAULTS['foo']",
                id='gargoyle.001',
            ),
        ]
