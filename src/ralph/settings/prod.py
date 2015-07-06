from ralph.settings import *  # noqa

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'  # noqa
STATIC_ROOT = os.path.join(BASE_DIR, 'var', 'static')

# FIXME: when going for full production, change it to False

DEBUG = True
