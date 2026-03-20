"""
Django settings for bergsolawi project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("JUNTAGRICO_SECRET_KEY")

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "intern.bergsolawi.ch",
    "bergsolawi.juntagrico.science",
    "localhost",
    "0.0.0.0",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "juntagrico_webdav",
    "juntagrico",
    "fontawesomefree",  # benötigt ab 1.6
    "import_export",  # benötigt ab 1.6
    "impersonate",
    "crispy_forms",
    "adminsortable2",
    "bergsolawi",
    "polymorphic",
]

ROOT_URLCONF = "bergsolawi.urls"

DATABASES = {
    "default": {
        "ENGINE": os.environ.get(
            "JUNTAGRICO_DATABASE_ENGINE", "django.db.backends.sqlite3"
        ),
        "NAME": os.environ.get("JUNTAGRICO_DATABASE_NAME", "bergsolawi.db"),
        "USER": os.environ.get(
            "JUNTAGRICO_DATABASE_USER"
        ),  #''junatagrico', # The following settings are not used with sqlite3:
        "PASSWORD": os.environ.get("JUNTAGRICO_DATABASE_PASSWORD"),  #''junatagrico',
        "HOST": os.environ.get(
            "JUNTAGRICO_DATABASE_HOST"
        ),  #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        "PORT": os.environ.get(
            "JUNTAGRICO_DATABASE_PORT", False
        ),  #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "juntagrico.context_processors.vocabulary",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "debug": True,
        },
    },
]

# The caches are for juntagrico_webdav, see
# https://github.com/juntagrico/juntagrico-webdav/blob/main/juntagrico_webdav/docs/instalation.rst
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "juntagrico_app_cache_table",
        "TIMEOUT": None,
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

WSGI_APPLICATION = "bergsolawi.wsgi.application"


LANGUAGE_CODE = "de"

SITE_ID = 7


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS = [
    "%d.%m.%Y",
]

AUTHENTICATION_BACKENDS = (
    "juntagrico.util.auth.AuthenticateWithEmail",
    "django.contrib.auth.backends.ModelBackend",
)


MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "impersonate.middleware.ImpersonateMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
]

DEFAULT_FROM_EMAIL = "info@bergsolawi.ch"

EMAIL_HOST = os.environ.get("JUNTAGRICO_EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("JUNTAGRICO_EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("JUNTAGRICO_EMAIL_PASSWORD")
EMAIL_PORT = int(os.environ.get("JUNTAGRICO_EMAIL_PORT", "25"))
EMAIL_USE_TLS = os.environ.get("JUNTAGRICO_EMAIL_TLS", "False") == "True"
EMAIL_USE_SSL = os.environ.get("JUNTAGRICO_EMAIL_SSL", "False") == "True"

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

WHITELIST_EMAILS = []


def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace("@gmail.com", "(\+\S+)?@gmail.com"))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)


STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

IMPERSONATE = {
    "REDIRECT_URL": "/my/profile",
}

LOGIN_REDIRECT_URL = "/"

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

MEDIA_ROOT = "media"

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = "bootstrap4"

"""
    import_export Settings
"""
# Berechtigung, die nötig ist um Einträge zu exportieren.
# Mit der Einstellung ‚view‘ können alle, die z.B. Abos im Admin sehen können,
# diese auch exportieren, was in den meisten Fällen passen sollte:

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = "view"

"""
     juntagrico Settings
"""
BUSINESS_YEAR_CANCELATION_MONTH = 2
MEMBERSHIP_END_MONTH = 5
BUSINESS_YEAR_START = {"day": 1, "month": 7}


ORGANISATION_NAME = "Bergsolawi"
ORGANISATION_LONG_NAME = "Genossenschaft Bergsolawi Surselva"
ORGANISATION_ADDRESS = {
    "name": "Genossenschaft Bergsolawi Surselva",
    "street": "Tobelhofstrasse",
    "number": "231",
    "zip": "8044",
    "city": "Zürich",
    "extra": "",
}
ORGANISATION_BANK_CONNECTION = {
    "PC": "123",
    "IBAN": "CH59 0839 0040 1694 1010 9",
    "BIC": "123",
    "NAME": "Alternative Bank Schweiz",
    "ESR": "",
}
SHARE_PRICE = "1111"

CONTACTS = {"general": "info@bergsolawi.ch"}
ORGANISATION_WEBSITE = {"name": "bergsolawi.ch", "url": "https://bergsolawi.ch"}
STYLES = {"static": ["bergsolawi/css/customize.css"]}
BYLAWS = "https://bergsolawi.ch/resources/statuten.pdf"

# See https://juntagrico.readthedocs.io/en/latest/settings.html#email
EMAILS = {
    "welcome": "mails/willkommen_mail.txt",
    "co_welcome": "mails/mitabonnent_willkommen.txt",
    # 'co_added': 'mails/added_mail.txt',
    "password": "mails/password_reset_mail.txt",
    # 'j_reminder': 'mails/job_reminder_mail.txt',
    # 'j_canceled': 'mails/job_canceled_mail.txt',
    # 'confirm': 'mails/confirm.txt',
    # 'j_changed': 'mails/job_time_changed_mail.txt',
    # 'j_signup': 'mails/job_signup_mail.txt',
    # 'd_changed': 'mails/depot_changed_mail.txt',
    "s_created": "mails/anteilsschein_mail.txt",
    # 'n_sub': 'mails/new_subscription.txt',
    "s_canceled": "mails/subscription_canceled_mail.txt",
    # 'm_canceled': 'mails/membership_canceled_mail.txt',
}
