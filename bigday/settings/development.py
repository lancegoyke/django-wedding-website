from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v1wd28@rtfs8z=*n)kf)+ekao0qdcz44o9)hndudi$_a2_1663'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# change to a real email backend in production
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
