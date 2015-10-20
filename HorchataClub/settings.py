
"""
Django settings for MaloBarba project.

Generated by 'django-admin startproject' using Django 1.8.4.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import environ

root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, True),) # set default values and casting
environ.Env.read_env() # reading .env file

SITE_ROOT = root()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = [
        '.arlefreak.club',
        '.horchata.club',
        'horchata.club',
        ]

# Application definition

INSTALLED_APPS = (
        'modeltranslation',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'corsheaders',
        'rest_framework',
        'taggit',
        'taggit_serializer',
        'ckeditor',
        'api',
        )

MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        )

ROOT_URLCONF = 'HorchataClub.urls'

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

WSGI_APPLICATION = 'HorchataClub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('DBNAME'),
            'USER': env('DBUSER'),
            'PASSWORD': env('DBPASSWD'),
            'HOST': 'localhost',
            'PORT': env('DBPORT'),
            }
        }



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/


LANGUAGE_CODE = 'en-us'
ugettext = lambda s: s
LANGUAGES = (
        ('es-Mx', ugettext('Spanish')),
        ('en', ugettext('English')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
        'default': {
        'toolbar': 'Basic',
                            },
}

CORS_ORIGIN_WHITELIST = (
        'horchata.club',
        'localhost',
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True
STATICFILES_STORAGE =  'storages.backends.s3boto.S3BotoStorage' 
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
COLLECTFAST_ENABLED = True
