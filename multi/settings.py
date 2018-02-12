import os
import dj_database_url
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for cloudmasterstudios project.

Generated by 'django-admin startproject' using Django 1.8.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from os.path import join, dirname


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ciao'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# The person to contact on error when DEBUG=False
ADMINS = [('pippo', 'ippo@io.io'),]

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

from multisite import SiteID
SITE_ID = SiteID(default=1)


ROOT_URLCONF = 'multi.urls1'



WSGI_APPLICATION = 'multi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'cloudmasterstudios', 'static'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'cloudmasterstudios', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings',
                'aldryn_boilerplates.context_processors.boilerplate',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
            ],
        },
    },
]


MIDDLEWARE_CLASSES = [
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'multisite.middleware.DynamicSiteMiddleware',
    'djangocms_multisite.middleware.CMSMultiSiteMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]

INSTALLED_APPS = [
    # Django & Django-CMS
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'reversion',
    # Django-CMS Blogging
    'aldryn_apphooks_config',
    'aldryn_boilerplates',
    'aldryn_categories',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_reversion',
    'aldryn_common',
    'parler',
    'sortedm2m',
    'taggit',
    'aldryn_disqus',
    'multisite',
    'djangocms_multisite',
    # Third Party
    'compressor',
    # Custom
    'multi',
]

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'redirect_on_fallback': True,
            'hide_untranslated': False,
            'code': 'en',
            'public': True,
            'name': gettext('en'),
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'hide_untranslated': False,
        'public': True,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'NAME': 'project.db',
        "ENGINE": "django.db.backends.sqlite3"
    }
}
#DATABASES['default'] = dj_database_url.config(default=env_var("DATABASE_URL"))

MIGRATION_MODULES = {
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

ALDRYN_BOILERPLATE_NAME='bootstrap3'

STATICFILES_FINDERS = [
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MULTISITE_CMS_URLS = {
    'www.example.com:8000': 'multi.urls1',
    'www.example2.com:8000': 'multi.urls2',
}
MULTISITE_CMS_ALIASES = {
    'www.example.com': ('alias1.example.com', 'alias2.example.com',),
    'www.example2.com': ('alias1.example2.com', 'alias2.example2.com',),
}
MULTISITE_CMS_FALLBACK = 'www.example.com'

# # The cache connection to use for django-multisite.
# # Default: 'default'
# CACHE_MULTISITE_ALIAS = 'multisite'
#
# # The cache key prefix that django-multisite should use.
# # Default: '' (Empty string)
# CACHE_MULTISITE_KEY_PREFIX = ''
#
#
#
# CACHES = {
#     'default': { # (PROD/QA)
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION': '127.0.0.1:11211',
#     },
#     'multisite': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'TIMEOUT': 60 * 60 * 24,  # 24 hours
#     },
# }
#
# # Django-CMS Caching
# # https://docs.django-cms.org/en/develop/how_to/caching.html
#
# CMS_CACHE_PREFIX = 'default'
