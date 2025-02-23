from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class EnvSettings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    CELERY_REDBEAT_REDIS_URL: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


env_settings = EnvSettings()

SECRET_KEY = env_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_settings.DEBUG

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main.apps.MainConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "rating.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rating.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env_settings.DB_NAME,
        "USER": env_settings.DB_USER,
        "PASSWORD": env_settings.DB_PASSWORD,
        "HOST": env_settings.DB_HOST,
        "PORT": env_settings.DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Celery

CELERY_BROKER_URL = env_settings.CELERY_BROKER_URL
CELERY_RESULT_BACKEND = env_settings.CELERY_RESULT_BACKEND

CELERY_BEAT_SCHEDULE = {
    "fetch_call_signs_every_day_at_midnight": {
        "task": "main.tasks.fetch_call_signs_and_save_to_db",
        "schedule": crontab(hour=0, minute=0),
    },
}
# CELERY_BEAT_SCHEDULE = {
#     "fetch_call_signs_every_day_at_midnight": {
#         "task": "main.tasks.fetch_call_signs_and_save_to_db",
#         "schedule": crontab(minute="*"),
#     },
# }
CELERY_BEAT_SCHEDULER = "redbeat.RedBeatScheduler"
CELERY_REDBEAT_KEY_PREFIX = "redbeat:"
CELERY_REDBEAT_REDIS_URL = env_settings.CELERY_REDBEAT_REDIS_URL

CELERY_TIMEZONE = TIME_ZONE
