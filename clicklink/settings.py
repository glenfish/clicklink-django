import os

# Application Name
APP_NAME = os.getenv('APP_NAME', 'DjangoApp')

# Environment
DEBUG = os.getenv('APP_ENV', 'production') != 'production'

# Timezone
TIME_ZONE = 'UTC'

# Language
LANGUAGE_CODE = 'en-us'

# Secret Key
SECRET_KEY = os.getenv('APP_KEY', 'your-secret-key')

ROOT_URLCONF = 'clicklink.urls'


# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clicklink',  # Your main app
]

# Middleware (Equivalent to Laravel Kernel.php)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Matches Laravel CheckForMaintenanceMode
    'django.contrib.sessions.middleware.SessionMiddleware',  # Matches Laravel StartSession
    'django.middleware.common.CommonMiddleware',  # Matches Laravel TrimStrings & ConvertEmptyStringsToNull
    'django.middleware.csrf.CsrfViewMiddleware',  # Matches Laravel EncryptCookies
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # Matches Laravel ShareErrorsFromSession
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'clicklink.middleware.CheckAdminMiddleware',  # Custom: Matches Laravel 'admin' Middleware
    'clicklink.middleware.CheckDeactivatedMiddleware',  # Custom: Matches Laravel 'check.deactivated' Middleware
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',  # Make sure this matches your database name
        'USER': 'postgres',  # Use the new user you created
        'PASSWORD': 'ecTgYr.Xa@@.chzNQbUZiaDB2F9YgV',  # Your new password
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Static & Media Files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Templates Configuration (Required for Django Admin)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ALLOWED_HOSTS = ['*']  # ✅ Allows all hosts (safe for local development)

DEBUG = True

AUTH_USER_MODEL = "clicklink.User"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Ensure this folder exists
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

