# Django settings for wolfscout project.


import os

PROJECT_DIR = os.path.split(os.path.realpath(os.path.dirname(__file__)))[0]
SITE_DIR = os.path.split(PROJECT_DIR)[0]

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR,  'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/media/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/opt/webapps/ncsu/wolfscout/static",
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')0vn)+cd7vdmra8qn1xzozq4mw9xoo9ni7g*9pvjqwxpm+@xhk'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'wolfscout.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates/'),
    '/opt/webapps/django/lib/python2.6/dist-packages/django/contrib/admin/templates/',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login/"
LOGOUT_URL = "/login/"
# set path to include apps subdir
import sys
sys.path.insert(0,os.path.join(PROJECT_DIR, 'apps'))

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.gis',
    'djangorestframework',
    #Locally Installed Apps
    'apps.crawler.cronos',
    'apps.crawler.gpscollar',
    'apps.study',
    'apps.wildlife',
	'apps.general',
    #Core Applications From Non-Django Sources
    'south',
    #Nose must be below south or it all fails
    'django_nose',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#Testing Configuration For Nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

#CSV Dictionary Mapping
CSV_DICTIONARY = {
    'GMT_DATETIME':(1, 2),
    'LMT_DATETIME' : (3, 4),
    'ECEF_X' : 5,
    'ECEF_Y' : 6,
    'ECEF_Z' : 7,
    'LATITUDE' : 8,
    'LONGITUDE' : 9,
    'HEIGHT' : 10,
    'DOP' : 11,
    'NAV' : 12,
    'VALIDATED' : 13,
    'SATS_USED' : 14,
    'CH1_SATID' : 15,
    'CH1_CN' : 16,
    'CH2_SATID' : 17,
    'CH2_CN' : 18,
    'CH3_SATID' : 19,
    'CH3_CN' : 20,
    'CH4_SATID' : 21,
    'CH4_CN' : 22,
    'CH5_SATID' : 23,
    'CH5_CN' : 24,
    'CH6_SATID' : 25,
    'CH6_CN' : 26,
    'CH7_SATID' : 27,
    'CH7_CN' : 28,
    'CH8_SATID' : 29,
    'CH8_CN' : 30,
    'CH9_SATID' : 31,
    'CH9_CN' : 32,
    'CH10_SATID' : 33,
    'CH10_CN' : 34,
    'CH11_SATID' : 35,
    'CH11_CN' : 36,
    'CH12_SATID' : 37,
    'CH12_CN' : 38,
    'MAIN_VOL' : 39,
    'BU_VOL' : 40,
    'TEMP' : 41,
    'REMARKS' : 42,
    'MAX_INDEX' : 42
}

CLIMATE_DICTIONARY = {
    # NEED ENTRIES FOR THESE:
    "id" : ("ID", ""),
    "distance_to_station" : ("Distance to Station", "(km)"),
    "station" : ("Station", ""),
    #####
    "lev1" : ("Level 1 Cloud Type / Height", ""),
    "lev2" : ("Level 2 Cloud Type / Height", ""),
    "lev3" : ("Level 3 Cloud Type / Height", ""),
    "ob" : ("observation date/time", "EST"),
    "temp" : ("Air Temperature", "(C)"),
    "tempmin" : ("Past Hour Min Temperature" , "(C)"),
    "tempmax" : ("Past Hour Max Temperature" , "(C)"),
    "tempavg" : ("Past Hour Avg Temperature" , "(C)"),
    "temp10" : ("10m Air Temperature", "(C)"),
    "temp10min" : ("Past Hour Min 10m Air Temperature", "(C)"),
    "temp10max" : ("Past Hour Max 10m Air Temperature", "(C)"),
    "temp10avg" : ("Past Hour Avg 10m Air Temperature", "(C)"),
    "tempmax6" : ("6 Hour Max Temperature", "(C)"),
    "tempmin6" : ("6 Hour Min Temperature", "(C)"),
    "tempmax24" : ("24 Hour Max Temperature", "(C)"),
    "tempmin24" : ("24 Hour Min Temperature", "(C)"),
    "rh" : ("Relative Humidity", "(%)"),
    "dew" : ("Dewpoint Temperature", "(C)"),
    "ws" : ("Wind Speed", "(m/s)"),
    "wd" : ("Wind Direction", "(deg)"),
    "gust" : ("Wind Gusts", "(m/s)"),
    "precip" : ("Hourly Precipitation", "(inch)"),
    "precip6" : ("3/6 Hour Precipitation", "(inch)"),
    "precip24" : ("24 Hour Total Precipitation", "(inch)"),
    "slp" : ("Sea Level Pressure", ""),
    "levl1" : ("Level 1 Cloud Type / Height", ""),
    "levl2" : ("Level 2 Cloud Type / Height", ""),
    "levl3" : ("Level 3 Cloud Type / Height", ""),
    "vis" : ("Visibility", "(sm)"),
    "weather" : ("Present Weather", ""),
    "obscur" : ("Obscuration", ""),
    "altimeter" : ("Altimeter Setting", "(in. hg)"),
    "presch" : ("Pressure Change", "(mb)"),
    "pind" : ("Pressure Indicator", ""),
    "groundsnow" : ("Snow On Ground", "(inch)"),
    "remarks" : ("METAR Remarks", ""),
    "rhmin" : ("Past Hour Min Relative Humidity", "(%)"),
    "rhmax" : ("Past Hour Max Relative Humidity", "(%)"),
    "rhavg" : ("Past Hour Avg Relative Humidity", "(%)"),
    "rh10" : ("10m Relative Humidity", "(C)"),
    "rh10min" : ("Past Hour Min 10m Relative Humidity", "(%)"),
    "rh10max" : ("Past Hour Max 10m Relative Humidity", "(%)"),
    "rh10avg" : ("Past Hour Avg 10m Relative Humidity", "(%)"),
    "wsavg" : ("Past Hour Avg Wind Speed", "(m/s)"),
    "ws02" : ("2m Wind Speed", "(m/s)"),
    "ws02avg" : ("Past Hour Avg 2m Wind Speed", "(m/s)"),
    "wdavg" : ("Past Hour Avg Wind Direction", "(deg)"),
    "wd02" : ("2m Wind Direction", "(deg)"),
    "wd02avg" : ("Past Hour Avg 2m Wind Direction", "(deg)"),
    "gustavg" : ("Past Hour Avg Wind Gusts", "(m/s)"),
    "pres" : ("Station Pressure", "(mb)"),
    "presmin" : ("Past Hour Min Station Pressure", "(mb)"),
    "presmax" : ("Past Hour Max Station Pressure", "(mb)"),
    "presavg" : ("Past Hour Avg Station Pressure", "(mb)"),
    "sr" : ("Solar Radiation", "(W / m^2)"),
    "srmin" : ("Past Hour Min Solar Radiation", "(W / m^2)"),
    "srmax" : ("Past Hour Max Solar Radiation", "(W / m^2)"),
    "sravg" : ("Past Hour Avg Solar Radiation", "(W / m^2)"),
    "par" : ("Photosynthetically Active Radation", "(W / m^2)"),
    "parmin" : ("Past Hour Min Photosynthetically Active Radiation ", "(W / m^2)"),
    "parmax" : ("Past Hour Max Photosynthetically Active Radiation ", "(W / m^2)"),
    "paravg" : ("Past Hour Avg Photosynthetically Active Radiation ", "(W / m^2)"),
    "st" : ("Soil Temperature", "(C)"),
    "stmin" : ("Past Hour Min Soil Temperature ", "(C)"),
    "stmax" : ("Past Hour Max Soil Temperature ", "(C)"),
    "stavg" : ("Past Hour Avg Soil Temperature ", "(C)"),
    "sm" : ("Soil Moisture", "(m^3 / m^3)"),
    "smmin" : ("Past Hour Min Soil Moisture", "(m^3 / m^3)"),
    "smmax" : ("Past Hour Max Soil Moisture", "(m^3 / m^3)"),
    "smavg" : ("Past Hour Avg Soil Moisture", "(m^3 / m^3)"),
    "leafwetness1" : ("Experimental Leaf Wetness", "(??)")
}

FIXTURE_DIRS = '/opt/webapps/ncsu/wolfscout/tests/data/fixtures'
CSV_UPLOAD_DIR = "/opt/webapps/ncsu/wolfscout/uploaded_files/"