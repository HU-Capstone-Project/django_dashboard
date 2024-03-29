from .settings import *

DEBUG = True
DATABASES["default"] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env("DB_NAME"),
    'USER': env("DB_USER"),
    'PASSWORD': env("DB_PASSWORD"),
    'HOST': env("DB_HOST"),
    'PORT': '5432',
}

ALLOWED_HOSTS = ["127.0.0.1",env("API_GATEWAY")]
DATABASES["default"]["ATOMIC_REQUESTS"] = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
INSTALLED_APPS += ["django_s3_storage"]
S3_BUCKET_NAME = env("S3_BUCKET_NAME")
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET_NAME
# serve the static files directly from the specified s3 bucket
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % S3_BUCKET_NAME
AWS_S3_PUBLIC_URL_STATIC = env("CLOUDFRONT_URL")
AWS_LOCATION = "static/"
STATIC_URL = AWS_S3_PUBLIC_URL_STATIC
AWS_S3_SECURE_URLS = True
AWS_S3_GZIP = True
