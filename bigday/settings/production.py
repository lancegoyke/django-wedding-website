from .base import *

from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_var("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    get_env_var("IP_ADDRESS"),
    get_env_var("DOMAIN"),
    'localhost',
]

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env_var('DB_NAME'),
        'USER': get_env_var('DB_USER'),
        'PASSWORD': get_env_var('DB_PASSWORD'),
        'HOST': get_env_var('DB_HOST'),
        'PORT': get_env_var('DB_PORT'),
    }
}

EMAIL_BACKEND = 'django_ses.SESBackend'
# Set the following environment variables
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY
# AWS_SES_REGION_NAME
# AWS_SES_REGION_ENDPOINT
