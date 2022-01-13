import dj_database_url

from .base import *

DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ["todo-django.herokuapp.com"]

# Security
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 15768000  # set low, but when site is ready for deployment, set to at least 15768000 (6 months)
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SAMESITE = 'Strict'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

CORS_ALLOWED_ORIGINS = [
    "https://todo-vue3.herokuapp.com"
]