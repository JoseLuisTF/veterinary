
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['veterinaryjoseluistf.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'd8ssbj7ba88718',
            'USER': 'hhwhagxqpungln',
            'PASSWORD': '053597db5f8be2bbe3b3a0ae110f4235681c75466a7499cc9eaa6580d8e2d6ec',
            'HOST': 'ec2-54-83-33-14.compute-1.amazonaws.com',
            'PORT': 5432,
        }
    }

STATICFILES_DIRS = (os.path.join(BASE_DIR, '../static'),)