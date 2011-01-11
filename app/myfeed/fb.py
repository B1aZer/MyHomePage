# Django settings for fbsample project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'db.sqlite3'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
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

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'yg6zh@+u^w3agtjwy^da)#277d3j#a%3m@)pev8_j0ozztwe4+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    'facebook.djangofb.FacebookMiddleware',
)

ROOT_URLCONF = 'fbsample.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    
    'fbsample.fbapp',
)

# get it from here 
# http://www.facebook.com/editapps.php?ref=mb
FACEBOOK_API_KEY = '184062098289427'
FACEBOOK_SECRET_KEY = '75fb6b2dadcfb90c3b4da7f7593d439b'
https://graph.facebook.com/oauth/authorize?
    client_id=184062098289427&
    redirect_uri=http://www.example.com/oauth_redirect
2.XVc7WMiPon41_rhkzzKkwQ__.3600.1294164000-586527073|i6HIy67vqhZnN9hiAflDqTfsfSc

https://graph.facebook.com/oauth/access_token?
    client_id=184062098289427&
    redirect_uri=http://b1azee.mine.nu&
    client_secret=75fb6b2dadcfb90c3b4da7f7593d439b&
    code=2.XVc7WMiPon41_rhkzzKkwQ__.3600.1294164000-586527073|i6HIy67vqhZnN9hiAflDqTfsfSc
o
https://graph.facebook.com/oauth/access_token?client_id=184062098289427&redirect_uri=http://b1azee.mine.nu/&client_secret=75fb6b2dadcfb90c3b4da7f7593d439b&code=2.XVc7WMiPon41_rhkzzKkwQ__.3600.1294164000-586527073|i6HIy67vqhZnN9hiAflDqTfsfSc
o

https://graph.facebook.com/oauth/authorize?client_id=184062098289427&scope=offline_access,read_stream&redirect_uri=http://www.facebook.com/connect/login_success.html
access_token=184062098289427|2.XVc7WMiPon41_rhkzzKkwQ__.3600.1294164000-586527073|ceFKr7u6EAEX25NoqzPvY2201co&expires=4175

1. https://graph.facebook.com/oauth/authorize?client_id=APP_ID&scope=offline_access,read_stream&redirect_uri=http://www.facebook.com/connect/login_success.html
2.  code = 581fb9c8dabc8880f5114c1a-586527073|hYJif4DmHT8aLlehdp0acTnPR-0
3. https://graph.facebook.com/oauth/access_token?client_id=184062098289427&redirect_uri=http://www.facebook.com/connect/login_success.html&client_secret=75fb6b2dadcfb90c3b4da7f7593d439b&code=581fb9c8dabc8880f5114c1a-586527073|hYJif4DmHT8aLlehdp0acTnPR-0
4. access_token=184062098289427|581fb9c8dabc8880f5114c1a-586527073|qZ5xs_S2_rwvaYsLXdXKZVwcST8