from os import getenv

from settings import *

DEBUG = False

secret_key_env = getenv("SECRET_KEY")

if not secret_key_env:
    raise Exception("SECRET_KEY not found or empty")

SECRET_KEY = ""

DATABASES = {
    "default": {
        "ENGINE": "",
        "NAME": ":memory:",
    }
}
