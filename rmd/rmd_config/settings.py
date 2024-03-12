"""
Django settings for rmd_config project.

Generated by 'django-admin startproject' using Django 5.0.2.

This settings file is organized into sections for easier navigation and understanding:
- Django and Project Basics
- Security Settings
- Application and Middleware Definitions
- Templates Configuration
- Database Configuration
- Authentication and User Management
- Internationalization
- Static Files Configuration
- Third-party Services Configuration (Firebase)

For more information on Django settings, see:
- https://docs.djangoproject.com/en/5.0/topics/settings/
- https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import firebase_admin
from firebase_admin import credentials

AUTH_USER_MODEL = 'rmd_web.User'

# Django and Project Basics
# ------------------------------------------------------------------------------

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s5hprzay$e0mipv--9eq#+5r7$kogjqn)3k__60#yx%1z8*w($'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Security Settings
# ------------------------------------------------------------------------------

# List of security settings here (e.g., SECURE_SSL_REDIRECT, CSRF_COOKIE_SECURE)


# Application and Middleware Definitions
# ------------------------------------------------------------------------------

INSTALLED_APPS = [
    # Required by allauth
    'django.contrib.sites', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    #
    'rmd_web',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     # Required by allauth
    'allauth.account.middleware.AccountMiddleware',  
    #
]

ROOT_URLCONF = 'rmd_config.urls'

# Templates Configuration
# ------------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rmd_config.wsgi.application'


# Database Configuration
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# ------------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Authentication and User Management
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/
# ------------------------------------------------------------------------------


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static Files Configuration (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
# ------------------------------------------------------------------------------

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Third-party Services Configuration (Firebase)
# ------------------------------------------------------------------------------

# Initialize Firebase Admin SDK
cred = credentials.Certificate("fire/rate-my-date-fca52-cf894cb26c1d.json")
firebase_admin.initialize_app(cred)


# Required by allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    # 'google': {
    #     'EMAIL_AUTHENTICATION': True
    # },
    # 'signup': 'allauth.socialaccount.forms.SignupForm',
}

SITE_ID = 1

# Optional allauth settings
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USERNAME_REQUIRED = True
LOGIN_REDIRECT_URL = '/'  # Redirect to home after login
# Pssibly delete data below
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_AUTHENTICATION_METHOD = 'EMAIL'
#
