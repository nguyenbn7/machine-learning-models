from os import getenv
from dotenv import load_dotenv

from api.settings import *

load_dotenv()

secret_key_env = getenv("SECRET_KEY")

allow_hosts_env = getenv("ALLOW_HOSTS")

if not secret_key_env:
    raise Exception("SECRET_KEY not found or empty")

if not allow_hosts_env:
    raise Exception("ALLOW_HOSTS not found or empty")

SECRET_KEY = secret_key_env

ALLOWED_HOSTS = list(map(lambda host: host.strip(), allow_hosts_env.split(",")))

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "rest_framework",
    "classification",
]

DEBUG = False


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


DATABASES = {}
