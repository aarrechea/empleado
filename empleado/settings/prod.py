# Droplet Digital Ocean connection
# root
# 146.190.34.238
# Z!cYYV5+ZbBDdB
# empleadodj


""" Imports """
from .base import *



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['146.190.34.238']



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} """

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'empleado',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR  / STATIC_URL]



""" Media files """
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'



