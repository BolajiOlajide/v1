import dj_database_url

from blog.settings.base import *


DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
