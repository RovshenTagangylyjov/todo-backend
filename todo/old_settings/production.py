import dj_database_url

from .base import *


DEBUG = False

ALLOWED_HOSTS = ["todo-django4.herokuapp.com"]

SECRET_KEY = os.getenv('SECRET_KEY')

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_ROOT = os.path.join(BASE_DIR, "assets")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CORS_ALLOWED_ORIGINS = [
    "https://todo-vue3.herokuapp.com"
]
