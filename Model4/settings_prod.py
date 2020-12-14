import os
from .settings import INSTALLED_APPS

DEBUG = False
ALLOWED_HOSTS = ['a-level-test.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DBNAME'),
        'USER': os.environ.get('DBUSER'),
        'PASSWORD': os.environ.get('DBPASS'),
        'HOST': os.environ.get('DBHOST', '127.0.0.1'),
        'PORT': os.environ.get('DBPORT', '5432'),
    }
}

INSTALLED_APPS.append('storages')

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get('S3_REGION')  # e.g. us-east-2
AWS_ACCESS_KEY_ID = os.environ.get('S3_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET')

# Tell django-storages the domain to use to refer to static files.
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_QUERYSTRING_AUTH = True
# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
