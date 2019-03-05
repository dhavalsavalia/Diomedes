"""
Django settings for diomedes project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = environ.Path(__file__) - 3
ROOT_DIR = BASE_DIR
APPS_DIR = ROOT_DIR.path('moviealert')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

env = environ.Env()

# This section added from an update to standards in CookieCutter
# Django to ensure no errors are encountered at runserver/migrations
# No need to read .env file explicityl in development mode
# Any specific development configuration which can not be commited
# should still be placed in .env files since `pipenv shell`
# will automatically export them
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)

if READ_DOT_ENV_FILE:
    env_file = str(ROOT_DIR.path('.env'))
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/


ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_rq',
    'anymail',
    'templated_mail',
    'django_extensions',
    'crispy_forms',
    'constance',
]

LOCAL_APPS = [
    'moviealert',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'diomedes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [APPS_DIR('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'diomedes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = { 'google': 
                             { 'SCOPE': ['email'],
                               'AUTH_PARAMS': { 'access_type': 'online',},
                               'VERIFIED_EMAIL':True,
                             }
                          }

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_GET = True

ANYMAIL = {
    "MAILGUN_API_KEY": os.environ['MAILGUN_API_KEY'],
    "MAILGUN_SENDER_DOMAIN": os.environ['MAILGUN_DOMAIN'],
}

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = "Diomedes <diomedes@getadomain.com>"
DEFAULT_REPLY_TO = "Diomedes <diomedes@getadomain.com>"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False, # keep Django's default loggers
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR('djangoproject.log'),
            'maxBytes': 50 * 10**6, # will 50 MB do?
            'backupCount': 3,
            'formatter': 'simple'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        # root configuration – for all of our own apps
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    },
}

LOGIN_REDIRECT_URL = 'task_view'

CONSTANCE_CONFIG = {
    'SEARCH_COUNT_LIMIT': (100, 'The number of days a movie should be searched for.', int),
}
