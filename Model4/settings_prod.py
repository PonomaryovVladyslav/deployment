import os
from .settings import INSTALLED_APPS

# DEBUG = False
# ALLOWED_HOSTS = ['34.221.249.152']

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
# print('IN_settings_prod')
#
# INSTALLED_APPS.append('storages')
#
# AWS_S3_OBJECT_PARAMETERS = {
#     'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#     'CacheControl': 'max-age=94608000',
# }
#
# AWS_STORAGE_BUCKET_NAME = 'a-level-deployment-test'
# AWS_S3_REGION_NAME = 'eu-central-1'  # e.g. us-east-2
# AWS_ACCESS_KEY_ID = 'AKIA5EGU72UMLRMVQRKM'
# AWS_SECRET_ACCESS_KEY = 'jOQddWDkc79rJp49o/rwvQzTv3dBoqYiDalqX+tk'
#
# # Tell django-storages the domain to use to refer to static files.
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#
# # Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# # you run `collectstatic`).
#
# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
#
# MEDIAFILES_LOCATION = 'media'
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
