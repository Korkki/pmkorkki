from __future__ import unicode_literals
import urlparse
from .base import *

ALLOWED_HOSTS = ['pmkorkki.herokuapp.com', 'localhost']

CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': os.environ.get('MEMCACHEDCLOUD_SERVERS').split(','),
        'OPTIONS': {
            'username': os.environ.get('MEMCACHEDCLOUD_USERNAME'),
            'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD')
        }
    }
}

REDIS_URL = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))

SESSION_ENGINE = 'redis_sessions.session'

SESSION_REDIS_HOST = REDIS_URL.hostname
SESSION_REDIS_PORT = REDIS_URL.port
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = REDIS_URL.password
SESSION_REDIS_PREFIX = 'session'