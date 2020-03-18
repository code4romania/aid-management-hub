"""
Django settings for ro_help project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _

import environ

root = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(f"{root}/.env")  # reading .env file

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "v*2$eed@gagp7f%kvb=zl%30c-(*gl9qppn0vv%sku#q7o&p64"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [".rohelp-102801068.eu-central-1.elb.amazonaws.com"]


# Application definition

INSTALLED_APPS = [
    "hub",
    "material.admin",
    "material.admin.default",
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "admin_auto_filters",
    "spurl",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "ro_help.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ro_help.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    "default": env.db("DATABASE_URL"),
    # read os.environ['SQLITE_URL']
    "extra": env.db("SQLITE_URL", default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3'),}",),
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LOCALE_PATHS = (os.path.join(BASE_DIR, "../", "locale"),)

LANGUAGE_CODE = "ro"

LANGUAGES = (
    ("en", "English"),
    ("ro", "Romanian"),
)

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../", "static"),
]


MATERIAL_ADMIN_SITE = {
    'HEADER':  _('COVID-19 RO HELP'),  # Admin site header
    'TITLE':  _('RO HELP'),  # Admin site title
    'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
    'MAIN_BG_COLOR':  '#fd4b49',  # Admin site main color, css color should be specified
    'MAIN_HOVER_COLOR':  '#fe9695',  # Admin site main hover color, css color should be specified
    'PROFILE_PICTURE':  'images/logo.png',  # Admin site profile picture (path to static should be specified)
    'PROFILE_BG':  'images/admin_background.svg',  # Admin site profile background (path to static should be specified)
    'LOGIN_LOGO':  'images/logo.png',  # Admin site logo on login page (path to static should be specified)
    'LOGOUT_BG':  'images/admin_background.svg',  # Admin site background on login/logout pages (path to static should be specified)
    'SHOW_THEMES':  False,  #  Show default admin themes button
    'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': True,  # Hide side navbar by default
    'SHOW_COUNTS': True, # Show instances counts for each model
    'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
        'sites': 'send',
    },
    'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
        'site': 'contact_mail',
        'hub': 'contact_mail',
    }
}