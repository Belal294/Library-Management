import os
from pathlib import Path
from datetime import timedelta
from decouple import config
from dotenv import load_dotenv
import dj_database_url

import cloudinary


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fqf2bs!-cv%bg$#vz_@$2b1mn7j!)e7)fim+ajr-wsm2#ah2k#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [".vercel.app", '127.0.0.1']

STATIC_ROOT = BASE_DIR / "staticfiles"
# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_yasg',
    'djoser',
    "debug_toolbar",
    'users',
    'books',
    'borrow',
    'api',
]

STATIC_URL = "static/"

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'library_management.urls'

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

WSGI_APPLICATION = 'library_management.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres', 
        'USER': 'postgres.ggroizbkitmdsraemmfm', 
        'PASSWORD': 'CTwsXwuFeoqNl7wv',  
        'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com', 
        'PORT': "5432",  
    }
}



cloudinary.config( 
    cloud_name = config('cloud_name'), 
    api_key = config('api_key'), 
    api_secret = config('api_secret_key'), 
    secure=True
)


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudynaryStorage'


STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('dbname'), 
#         'USER': config('user'), 
#         'PASSWORD': config('password'),  
#         'HOST': config('host'), 
#         'PORT': config('port'),  
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': "django.db.backends.postgresql_psycopg2",
#         'NAME': "postgres", 
#         'USER': "postgres.sageugkdjyjbxnezguwc", 
#         'PASSWORD': "Didar4048@",  
#         'HOST': "aws-0-ap-southeast-1.pooler.supabase.com", 
#         'PORT': "5432",  
#     }
# }


# DATABASES = {
#     "default": dj_database_url.config(
#         default=os.getenv("postgresql://postgres:Didar4048@@db.uexnhvtjcjvtgnjgsbry.supabase.co:5432/postgres"),
#         conn_max_age=600,
#         ssl_require=True
#     )
# }


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    

    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ]
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTH_USER_MODEL = 'users.CustomUser'

AUTH_USER_MODEL = 'users.CustomUser'



SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
   "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
}



DJOSER = {
    'SERIALIZERS':{
        'user_create' : 'users.serializers.UserCreateSerializer',
        'current_user' : 'users.serializers.UserSerializer'
    }
}



SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description':'Enter Your JWT token in the format: `JWT <your_token>`',
      }
   }
}
