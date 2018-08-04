from django.core.checks import register, Warning
from django.conf import settings

@register
def check_default_switch_status(app_configs, **kwargs):
    errors = []
    if hasattr(settings, 'GARGOYLE_SWITCH_DEFAULTS'):
        for key, switch_defaults in settings.GARGOYLE_SWITCH_DEFAULTS.iteritems():
            if 'is_active' in switch_defaults and 'initial_status' in switch_defaults:
                errors.append(Warning(
                    '"is_active" will take precedence over "initial_status" in GARGOYLE_SWITCH_DEFAULTS.',
                    hint='settings.GARGOYLE_SWITCH_DEFAULTS[\'{}\']'.format(key),
                ))
    return errors
