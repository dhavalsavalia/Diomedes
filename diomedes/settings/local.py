from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default=")!c%it$!hd0g=2&qfr!8)_zlu!7-!5g#5s8mu*xb2w2o@=x!dc")

DEBUG = env.bool('DJANGO_DEBUG', default=True)