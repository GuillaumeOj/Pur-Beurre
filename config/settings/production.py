"""Django settings for the local project."""
import os

import dj_database_url
from dotenv import load_dotenv, find_dotenv

# Import the base settings
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [".ojardias.io"]

# Heroku database
if os.environ.get("ENV_HOST") == "HEROKU":
    SECRET_KEY = os.environ["SECRET_KEY"]
    MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware",)

    DATABASE_URL = os.environ["DATABASE_URL"]
    DATABASES = {}
    DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)

    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

else:
    load_dotenv(find_dotenv())
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT"),
        }
    }
