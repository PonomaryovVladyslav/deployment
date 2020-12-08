import os
from .settings import INSTALLED_APPS
DEBUG = False
ALLOWED_HOSTS = ['54.202.36.120']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('database_name'),
        'USER': os.environ.get('database_user'),
        'PASSWORD': os.environ.get('database_password'),
        'HOST': os.environ.get('database_host', '127.0.0.1'),
        'PORT': os.environ.get('database_port', '5432'),
    }
}

INSTALLED_APPS.append('storages')

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = 'a-level-deployment-test'
AWS_S3_REGION_NAME = 'eu-central-1'  # e.g. us-east-2
AWS_ACCESS_KEY_ID = 'AKIA5EGU72UMLRMVQRKM'
AWS_SECRET_ACCESS_KEY = 'jOQddWDkc79rJp49o/rwvQzTv3dBoqYiDalqX+tk'

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'