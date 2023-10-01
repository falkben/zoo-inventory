from .settings import *

# Override STATICFILES_STORAGE setting
# Avoid "ValueError: Missing staticfiles manifest entry" during testing
# see: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#django.contrib.staticfiles.storage.ManifestStaticFilesStorage.manifest_strict
STORAGES = {
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# faster password hashing for test
# can also get around this by doing force_login()
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
