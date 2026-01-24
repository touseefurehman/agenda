
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
import cloudinary
SECRET_KEY = 'django-insecure-m_t-npj$g)dwkb!3^ku%0h2*j^6an!#a&2x$bo+)4l%q#n&il1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["agenda.up.railway.app",'*']


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'events',
    'import_export',
    'cloudinary',
    'cloudinary_storage',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'core.urls'

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 👈 add this
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',   # 👈 media
            ],
        },
    },
]


WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',   # 👈 project-level static
]

STATIC_ROOT = BASE_DIR / 'staticfiles'  # 👈 for production


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CSRF_TRUSTED_ORIGINS = [
    "https://agenda.up.railway.app",  # your deployed URL
]

JAZZMIN_SETTINGS = {
    "site_title": "Admin",
    "site_header": "Global Currency Forum",
    "site_brand": "Global Currency Forum",
    "site_logo": "images/admin_logo.png",

    "theme": "darkly",
    "navigation_expanded": True,
    "show_ui_builder": True,

    "welcome_sign": "Welcome to Global Currency Forum Admin",

    # 🔥 THIS IS THE IMPORTANT PART
    "icons": {
        # Django default
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",

        # Events app (use your actual app name)
        "events": "fas fa-calendar-alt",
        "events.event": "fas fa-calendar",
        "events.eventdays": "fas fa-calendar-day",
        "events.speaker": "fas fa-microphone",
    },
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'djm9pvxo5',
    'API_KEY': '199526248914836',
    'API_SECRET': 'rhZ69LN-37sZtuKY65hSMo3S5iI',
}

cloudinary.config(
    cloud_name = CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key = CLOUDINARY_STORAGE['API_KEY'],
    api_secret = CLOUDINARY_STORAGE['API_SECRET'],
    secure = True
)