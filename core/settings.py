from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-7w^$!y0q9+@4lyt$ncm48mz%c*m44hs9&9miabbkvy*))bmsqg'

DEBUG = True

ALLOWED_HOSTS = []


# APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # LOCAL APPS
    'leads',
    'agents',
]


# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'


# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # /templates is the directory name that contains the templates
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

WSGI_APPLICATION = 'core.wsgi.application'


# DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validators
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static' # /static is the directory name that contains the static files. DOES NOTHING ON DEPLOYMENT
]
STATIC_ROOT = 'static_root' # defines the single folder you want to collect all your static files into. ONLY REQUIRED FOR DEPLOYMENT
# is the folder where files uploaded using FileField will go.   

# I dont know what this is!!!
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom UserModel or subclassed User
AUTH_USER_MODEL = 'leads.User'

# Email sending function
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# after logging in, will be redirected to 'leads:home'
LOGIN_REDIRECT_URL = 'leads:home'

# after logging out, user will be redirected to 'leads:landingpage'
LOGOUT_REDIRECT_URL = 'leads:landingpage'

# if user isn't permitted, user will be redirected to 'leads:landingpage'
LOGIN_URL = 'leads:landingpage'