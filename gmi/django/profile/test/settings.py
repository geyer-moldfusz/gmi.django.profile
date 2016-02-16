INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sites',
    'django_markdown',
    'gmi.django.avatar',
    'gmi.django.profile',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

SECRET_KEY = 'xxx'

SITE_ID = 1

STATIC_URL = '/static/'

ROOT_URLCONF = 'gmi.django.profile.test.urls'
