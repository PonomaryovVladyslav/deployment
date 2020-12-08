import os
DEBUG = False
ALLOWED_HOSTS = ['*']

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