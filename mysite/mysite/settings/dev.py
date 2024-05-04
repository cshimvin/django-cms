from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+6p&#gw9#6q=!%8$$uf=2#+o@^qmoa27bwi0i7vr@o^et9l07s"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass

CSRF_TRUSTED_ORIGINS = ['https://8000-cshimvin-djangocms-tfvu5eoxfd0.ws-eu111.gitpod.io']