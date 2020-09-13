# Import the base settings
from .base import *


ALLOWED_HOSTS = ["*"]


SECRET_KEY = "foo_key_for_travis"
DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}
