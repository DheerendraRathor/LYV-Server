# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<SECRET KEY>'

DEBUG = False

ALLOWED_HOSTS = ['lyv.abhyuday-iitb.org']

MEDIA_URL = "/media/"

STATIC_URL = "/static/"

SESSION_COOKIE_PATH = "/"

CSRF_COOKIE_PATH = "/"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
