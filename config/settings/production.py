"""
Django settings for the local project.
"""
import os

import dj_database_url
import django_heroku

from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [".ojardias.io", "fast-shore-25529.herokuapp.com"]

# Heroku database
DATABASE_URL = os.environ["DATABASE_URL"]
DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)

django_heroku.settings(locals())
