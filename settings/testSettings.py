from common import *


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'wolfscout',                      # Or path to database file if using sqlite3.
        'USER': 'postgres',                     # Not used with sqlite3.
        'PASSWORD': 'thewolfhowlsatcows',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DEFAULT_INTERACTION_DISTANCE = .5
TEST_RUNNER = 'django.contrib.gis.tests.GeoDjangoTestSuiteRunner'
CRONOS_API_KEY = 'b503730e2a6b5869531352324580cd62ff123dab019694a99f239907ebe4b'
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'