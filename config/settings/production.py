"""Django settings for the local project."""
import os

import dj_database_url
import environ

# Import the base settings
from .base import *

ENV = environ.Env()
environ.Env.read_env()

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

elif ENV("ENV_HOST") == "OCEAN":
    SECRET_KEY = ENV("SECRET_KEY")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": ENV("DATABASE_NAME"),
            "USER": ENV("DATABASE_USER"),
            "PASSWORD": ENV("DATABASE_PASSWORD"),
            "HOST": ENV("DATABASE_HOST"),
            "PORT": ENV("DATABASE_PORT"),
        }
    }
