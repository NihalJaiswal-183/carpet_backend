from pathlib import Path
import os
import firebase_admin
import pyrebase
from firebase_admin import credentials


CORS_ALLOW_ALL_ORIGINS = True
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




# Firebase settings
FIREBASE_CREDENTIALS_PATH = os.path.join(BASE_DIR, 'firebase_key.json')
FIREBASE_APP = None
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\nihal\\Desktop\\carpet_backend\\carpet_backend\\firebase_key.json"
try:
    cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "carpet-backend",
    "private_key_id": "002787380be525fc08de8e3862207564412bb811",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC68NnarYMVL8TW\nP5rkOdS3S218mDbMk/ADtL75BTlLGg/+44vb5Calnc1o78pfeVPN0kV/8i0+LtI2\nIOmFl+xYqGFiCU0/+ZoVIv7BWi33VGVOJw2J0SpvtJapCzFUGy+aeht1r9smGvZ3\nfYFtPyuYDUM3A3sxKlccQYEb/y1XIXAoS57UF94sPC2jp7hBYhVll6K6p+mHbRDq\nepOKAiToybIqwuXSL4Hau7U6JMYRjqXPJW3EVKdJ/VDST1/eO8+qFAPcXDHR5kFK\nKoiUzhegBAkBKjzK+Fkpe9rFM4SB8HFbE0zCWfI6K9aGffrltzNcqxoNKZyGlinN\nQY6KE7dhAgMBAAECggEADx6/dCdAGLTYJh8XY1nFGX01khQKrKHTki0qnCAeyfMF\n868KZyLtOEyK6m+ore+1hkp5WhenrqWhVYT0dlx7HpGh7MjFUYUaABcoRVHKsXxH\nRFq2xtye4tGXtP0FhKC9STCSq4Jphou8Px5s2z32g/Igq2Cx9GBREuU+cNoDHA6h\n/Y9rSL6fKJqB5Nl3LuQFgxZ1MradN1oBXJoWPImDprSJlRvF5b6UJJrLn87SoGpL\nWxWpiYi+nRVokiplaak+odeRRIvtkCmTxTsL/gYHMtD39c8R+s0T/vDYcCcBdBxj\nTsaD2aISWaFJMTxzbCYeuicsHICzQa8HAahA5djLkQKBgQDyVsXMslDHcZkqj1wd\nU6+wdWnhGN5eQ+VoiGJdPHR1cQLpijQZd0SJI0HbtuURDULIee7/+LHinrCSoo8X\nHZuf8N0Gf78sFiHal3kAZ5hzM+VoxBR61Q5UGVwrGf63J0Rh2Rs6dhfkL3J/8Ctc\nsTH+8QZRoF/Oo4XfS4jyBYCj2QKBgQDFep7CuuCnU1yiWehI6xpqGbnbzLTdc5jQ\n+2jifjLYbG4ctsGg5pzJjDf56ecNeEGvdVojHy9Jojs3Z03YZChBcY84LfyzoKSK\nr+a0wvi1FF8cUcD5TQYHVPndba5bDu3Rdv2PGONQFnP+v9+rCOVRYmNRelUDqDPQ\noA/gvepiyQKBgGSsu7uQEJLqlHDj4aalT4WFIZlL1YVfu3wzvHlzVgY8DrOqoH47\n2BMIvKFkV8E/uxDB5xIb5Pp6ZmxkcAFwYWiOjaPXijnsb9/5sWEDqIejdZiSbNei\njzNM3cdiIzk/bN8hbHha+w3m0DBqO/lj+5sn0jIy59pWgJUFMj0pIAnxAoGAc0ZQ\nxnswCHyw5lR1M5uJn8XEqHmmWl7QJa2cXBoutAcXf8tu2+3COCSRyGCxbztznGh0\nZWwevmzlBEJZPqe4l/siDzlI+dIcOpjTo1DsvUdW/cD7VIuRqVYBRTBxRtZAHLXI\n7W8pweZZb6uxdLWMpyU3tKgkWC4nkPDeU+KIn4ECgYA+3NO5jhMGCB083EnRd/9j\n698GCAaIKr18jx9evWbj1ueW3y9sRWUSCykP9dKPXOMWoSM6UTj+Ag4WvqXF4HG7\nMM0b5vTkkjj3Zz7nx8QYMkiXBcG1E/CgDKyN3aXZOXRo5zdIzxAA3KqG0HTqVSyR\nCei39oK2YoclHVVjEJfr9A==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-c55ut@carpet-backend.iam.gserviceaccount.com",
    "client_id": "107685603975566237206",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-c55ut%40carpet-backend.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
  })
    FIREBASE_APP = firebase_admin.initialize_app(cred)
    print("Firebase Admin SDK initialized successfully.")
except ValueError as e:
    print("Firebase initialization error:", e)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8anzvzu_^n3^_o_)#y(e0_9i%&ac#n&=7n81p(^g=f$osa_y6('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken', 
    'django.contrib.sites',
]

CUSTOM_APPS = [
    "accounts"
]

INSTALLED_APPS =  DEFAULT_APPS + CUSTOM_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'carpet_backend.urls'

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

WSGI_APPLICATION = 'carpet_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'accounts.auth_verify.FirebaseAuthentication',  # Your custom authentication class
        'rest_framework.authentication.SessionAuthentication',  # Default session authentication
        'rest_framework.authentication.BasicAuthentication',   # Default basic authentication
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Default permission for authenticated users
        'rest_framework.permissions.AllowAny',  # Default permission allowing access to anyone
    ],
}



