import os

# Default to development settings
DJANGO_SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE', 'dojo.settings.dev')

if DJANGO_SETTINGS_MODULE == 'dojo.settings.dev':
    from .dev import *
elif DJANGO_SETTINGS_MODULE == 'dojo.settings.prod':
    from .prod import *
else:
    # Fallback to development settings
    from .dev import *
