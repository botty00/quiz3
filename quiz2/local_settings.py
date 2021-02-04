import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'k@&ox@_35&$70=3tflb!8nbp)=wht52ej6g^grv+lti82(keem'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'base',
        'USER': 'postgres',
        'PASSWORD': '0305post',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


DEBUG = True