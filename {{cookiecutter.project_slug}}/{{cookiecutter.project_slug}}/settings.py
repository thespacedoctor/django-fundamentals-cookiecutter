"""*Django settings for {{ cookiecutter.project_name }}, built on django_fundamentals*"""

import os
from pathlib import Path

from django_fundamentals.settings import (
    BASE_AUTHENTICATION_BACKENDS,
    BASE_INSTALLED_APPS,
    BASE_MIDDLEWARE,
    BASE_REST_FRAMEWORK,
    BASE_TEMPLATE_CONTEXT_PROCESSORS,
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "change-me-in-production"  # OVERRIDE VIA ENV VAR IN DEPLOY
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "{{ cookiecutter.deploy_host }}"]

AUTH_USER_MODEL = "django_fundamentals.User"
SITE_ID = 1

INSTALLED_APPS = [*BASE_INSTALLED_APPS]
MIDDLEWARE = [*BASE_MIDDLEWARE]
AUTHENTICATION_BACKENDS = BASE_AUTHENTICATION_BACKENDS
REST_FRAMEWORK = BASE_REST_FRAMEWORK

ROOT_URLCONF = "{{ cookiecutter.project_slug }}.urls"
WSGI_APPLICATION = "{{ cookiecutter.project_slug }}.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": BASE_TEMPLATE_CONTEXT_PROCESSORS},
    }
]

{%- if cookiecutter.database_backend == "sqlite_dev_mariadb_prod" %}

if os.environ.get("DJANGO_ENV") == "production":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ.get("DB_NAME", "{{ cookiecutter.project_slug }}"),
            "USER": os.environ.get("DB_USER", "{{ cookiecutter.project_slug }}"),
            "PASSWORD": os.environ.get("DB_PASSWORD", ""),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", "3306"),
            "OPTIONS": {"charset": "utf8mb4"},
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
{%- else %}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
{%- endif %}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
