from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

DEFAULT_SETTINGS = {
    'METADATA_FORM': 'vintage.metadata_form.MetadataForm',
}

USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'VINTAGE_SETTINGS', {}))

if not USER_SETTINGS['METADATA_FORM']:
    raise ImproperlyConfigured('The METADATA_FORM setting should be a python path to a Django Form class.')

bits = USER_SETTINGS['METADATA_FORM'].split('.')
importpath, classname = ".".join(bits[:-1]), bits[-1]
USER_SETTINGS['METADATA_FORM'] = getattr(import_module(importpath), classname)

globals().update(USER_SETTINGS)