"""
Django settings for django apps project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rk+=2d(9d87(zg1_!(u!6d)8%6pmwo-l&fet8111^&!f&=*x0q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['django.localhost', 'inchiresolver.localhost']


# Application definition

INSTALLED_APPS = [

    'resolver',
    'inchi',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',

    # last application to finalize things
    'finalware',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'apps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR,
            os.path.join(BASE_DIR, 'resolver', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'finalware.context_processors.contextify',
            ],
        },
    },
]

WSGI_APPLICATION = 'apps.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', 
            'NAME': 'appserver',
            'USER':  'appserver',
            'PASSWORD': os.environ['POSTGRES_APPSERVERDB_PASSWORD'],
            'HOST': os.environ['POSTGRES_APPSERVERDB_HOST'],
            'PORT': 5432
        },
    'appserverdb': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', 
            'NAME': 'appserver',
            'USER':  'appserver',
            'PASSWORD': os.environ['POSTGRES_APPSERVERDB_PASSWORD'],
            'HOST': os.environ['POSTGRES_APPSERVERDB_HOST'],
            'PORT': 5432
        }
}
#DATABASE_ROUTERS = ['apps.dbrouter.AuthRouter',]

# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join("/home/service", "static/")

MEDIA_ROOT = os.path.join("/home/service", "media/")
MEDIA_URL = "/media/"


# Add `SITE_OBJECTS_INFO_DICT` to your settings file. For example:
SITE_OBJECTS_INFO_DICT = {
    '1': {
        'name': os.environ['DJANGO_HOSTNAME'],
        'domain': os.environ['DJANGO_HOSTNAME'],
    },
}
SITE_ID = 1

# To create/update a superuser account automatically, add the following to your settings file.
# This will disable the `superuser` creation option of syncdb.

# This field is the superuser object ID. Pick something other than `1` for security reason.
SITE_SUPERUSER_ID = '987'

# This field is stored in `User.USERNAME_FIELD`. This is usually a `username` or  an `email`.
SITE_SUPERUSER_USERNAME = 'djangoadmin'

# This field is stored in the `email` field, provided, that `User.USERNAME_FIELD` is not an `email`.
# If `User.USERNAME_FIELD` is already an email address, set `SITE_SUPERUSER_EMAIL = SITE_SUPERUSER_USERNAME`
SITE_SUPERUSER_EMAIL = 'django@django'

# A hashed version of `SITE_SUPERUSER_PASSWORD` will be store in superuser's `password` field.
SITE_SUPERUSER_PASSWORD = 'djangoDJANGO'


