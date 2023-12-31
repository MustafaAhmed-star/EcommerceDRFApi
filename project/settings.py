
from datetime import timedelta
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9i5k83ce&i#=4k*d8tm^+u*bjn)!rve-z&c0rjkz*5xn^p62-6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # i make it false to run error handling

ALLOWED_HOSTS = ['localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ######
    'account',
    'rest_framework',
    'product',
    'django_filters',
    'rest_framework_simplejwt',#If you wish to use localizations/translations, simply add rest_framework_simplejwt to INSTALLED_APPS.
    'order',
]
REST_FRAMEWORK = {
     
    'DEFAULT_AUTHENTICATION_CLASSES': (
       
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
  }

SIMPLE_JWT= {
    'ACCESS_TOKEN_LIFETIME':timedelta(days = 10),
    'REFRESH_TOKEN_LIFETIME':timedelta(days=1),
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADERS_TYPES':('Bearer',),
    'AUTH_TOKEN_CLASSES':('rest_framework_simplejwt.tokens.AccessToken',),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
 
LANGUAGES = [
    ('en', _('English')),
    ('zh-hans', _('Simplified Chinese')),
]
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'c151624c22483e'
EMAIL_HOST_PASSWORD = 'aa8dd99114ffbb'
EMAIL_PORT = '2525'
EMAIL_USE_TLS: False
EMAIL_USE_SSL: False