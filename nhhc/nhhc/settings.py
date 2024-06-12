"""
Django settings for nhhc project.

Generated by 'django-admin startproject' using Django 3.2.20.

"""

import os
import sys
from pathlib import Path

import highlight_io
from highlight_io.integrations.django import DjangoIntegration
from logtail import LogtailHandler
from loguru import logger

TESTING = "test" in sys.argv

logger.remove()  # Remove all handlers added so far, including the default one.

# SECTION - Basic Application Defintion
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ["SECRET_KEY"]
# DEBUG = bool(os.environ["ENABLE_DEBUGGING"])
DEBUG: bool = True
KOLO_DISABLE = not DEBUG
DATETIME_FORMAT: str = "m/d/yyyy h:mm A"
ADMINS = [("Terry Brooks", "Terry@BrooksJr.com")]
MANAGERS = ADMINS
WSGI_APPLICATION = "nhhc.wsgi.application"
ROBOTS_USE_HOST = False
FIRST_DAY_OF_WEEK = 1
RECAPTCHA_PUBLIC_KEY = os.environ["RECAPTCHA_PUBLIC_KEY"]
RECAPTCHA_PRIVATE_KEY = os.environ["RECAPTCHA_PRIVATE_KEY"]
SILENCED_SYSTEM_CHECKS = ["auth.W004"]
ROBOTS_SITEMAP_VIEW_NAME = "cached-sitemap"
SITE_ID = os.environ["SITE_ID"]
ENVIRONMENT_FLOAT = True
ENVIRONMENT_NAME = os.environ["ENVIRONMENT_NAME"]
ENVIRONMENT_COLOR = os.environ["ENVIRONMENT_COLOR"]
REQUEST_BASE_URL = os.environ["REQUEST_BASE_URL"]
ROOT_URLCONF = "nhhc.urls"

# SECTION - CORS and CSFR Settings
REFERRER_POLICY = "strict-origin-when-cross-origin"
CSRF_COOKIE_NAME = "nhhc-csrf"
CSRF_FAILURE_VIEW = "nhhc.urls.permission_denied_handler"
SESSION_COOKIE_NAME = "nhhc-session"
CSRF_HEADER_NAME = "X_CSRFToken"
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^null$",
    r"^http://localhost:[0-9]+$",
    r"^http://127\\.0\\.0\\.1:[0-9]+$",
    r"^https://localhost:[0-9]+$",
    r"^https://127\\.0\\.0\\.1:[0-9]+$",
    r"^https://docuseal.s3.amazonaws.com/*",
]


CSRF_COOKIE_SECURE = False
CORS_ALLOW_PRIVATE_NETWORK = True
CSRF_COOKIE_DOMAIN = None
SESSION_COOKIE_SECURE = False
CORS_ORIGIN_ALLOW_ALL = True
SESSION_COOKIE_HTTPONLY = False
CORS_ALLOW_CREDENTIALS = True
# CSRF_TRUSTED_ORIGINS = ["http://localhost"]


# !SECTION

# SECTION - Protcols, ACL COnfigs
ADMINRESTRICT_ALLOW_PRIVATE_IP = False
ALLOWED_HOSTS = list(os.environ["ALLOWED_HOSTS"].split(","))
RESTRICT_ADMIN_BY_IPS = True
ALLOWED_ADMIN_IPS = list(os.environ["ALLOWED_IPS"].split(","))
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
INTERNAL_IPS = ["127.0.0.1"]


# SECTION - Email Communication
if DEBUG:
    EMAIL_BACKEND = "mail_panel.backend.MailToolbarBackend"
else:
    EMAIL_BACKEND = "django_smtp_ssl.SSLEmailBackend"


EMAIL_HOST = os.environ["EMAIL_SERVER"]
EMAIL_USE_TLS = False
EMAIL_USE_LOCALTIME = True
DEFAULT_FROM_EMAIL = "postmaster@netthandshome.care"
SERVER_EMAIL = DEFAULT_FROM_EMAIL
INTERNAL_SUBMISSION_NOTIFICATION_EMAILS = list(os.environ["INTERNAL_NOTIFICATION_EMAILS"].split(","))
EMAIL_PORT = os.environ["EMAIL_SSL_PORT"]
EMAIL_HOST_USER = os.environ["EMAIL_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_ACCT_PASSWORD"]
AWS_SES_SECRET_ACCESS_KEY = os.environ["AWS_SES_SECRET_ACCESS_KEY"]


# !SECTION

APPEND_SLASH = True
CRISPY_ALLOWED_TEMPLATE_PACKS = (
    "bootstrap",
    "uni_form",
    "bootstrap5",
    "bootstrap4",
)
SITE_ID = int(os.environ["SITE_ID"])
TINYMCE_JS_URL = f'https://cdn.tiny.cloud/1/{os.environ["TINYMCE_API_KEY"]}/tinymce/7/tinymce.min.js'
TINYMCE_COMPRESSOR = True
CRISPY_TEMPLATE_PACK = "bootstrap5"
TINYMCE_SPELLCHECKER = True
TINYMCE_DEFAULT_CONFIG = {
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code " "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save  | insertfile image media pageembed template link anchor codesample | "
    "| showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "en",  # To force a specific language instead of the Django current language.
}
INSTALLED_APPS = [
    "kolo",
    "whitenoise.runserver_nostatic",
    "allauth",
    "allauth.account",
    "jazzmin",
    "django_admin_env_notice",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    ## Installed 3rd Apps
    "crispy_forms",
    "crispy_bootstrap5",
    "storages",
    "phonenumber_field",
    "widget_tweaks",
    "django_prometheus",
    "rest_framework",
    "rest_framework.authtoken",
    "request",
    "formset",
    "django_filters",
    "localflavor",
    "captcha",
    "django_celery_beat",
    "corsheaders",
    "tinymce",
    "robots",
    # "IpWhitelister",
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.contrib.s3boto3_storage",
    "health_check.contrib.redis",
    "sage_encrypt",
    "anymail",
    "health_check.storage",
    "django_celery_results",
    "health_check.contrib.migrations",
    ## Installed Internal Apps
    "web",
    "portal",
    "employee",
    "announcements",
    "nhhc",
    "authentication",
    "compliance",
    "django_extensions",
]

# if DEBUG is False:
#     INSTALLED_APPS= ["kolo","debug_toolbar","coverage" ]  + INSTALLED_APPS

MIDDLEWARE = [
    "kolo.middleware.KoloMiddleware",
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django_referrer_policy.middleware.ReferrerPolicyMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "request.middleware.RequestMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

# SECTION - Database and Caching
CACHE_TTL: int = int(os.environ["TIME_TO_LIVE_MINUTES"]) * 60
QUERYSET_TTL: int = int(os.environ["QUERYSET_TTL"])

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # "ENGINE": "django_prometheus.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DATABASE"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "PORT": 5432,
        "HOST": os.environ["POSTGRES_HOST"],
        "OPTIONS": {"sslmode": "require"},
    },
}
# SECTION - Database Encryption
ENCRYPT_KEY = os.environ["ENCRYPT_KEY"]
ENCRYPT_PRIVATE_KEY = os.environ["DB_GPG_PRIVATE_KEY"]
ENCRYPT_PUBLIC_KEY = os.environ["DB_GPG_PUBLIC_KEY"]
# !SECTION

# Section - Caching
REDIS_URL = os.environ["REDIS_CACHE_URI_TOKEN"]
HEALTHCHECK_CACHE_KEY = "healthcheck_key"

CACHES = {
    "default": {
        "BACKEND": os.environ["CACHE_ENGINE"],
        "LOCATION": os.environ["REDIS_CACHE_URI_TOKEN"],
        "OPTIONS": {
            "PARSER_CLASS": os.environ["CACHE_PARSER"],
        },
        "KEY_PREFIX": "NHHC-NATIVE",
    },
    "celery": {
        "BACKEND": os.environ["CACHE_ENGINE"],
        "LOCATION": f'{os.environ["REDIS_CACHE_URI_TOKEN"]}/3',
        "OPTIONS": {
            "PARSER_CLASS": os.environ["CACHE_PARSER"],
        },
        "KEY_PREFIX": "C-TASK",
    },
}
ROBOTS_CACHE_TIMEOUT = 60 * 60 * 24


# !SECTION

# !SECTION

# SECTION - Password validation
AUTH_USER_MODEL = "employee.Employee"
AUTH_PROFILE_MODULE = "authentication.UserProfile"
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
ADMINRESTRICT_ENABLE_CACHE = True
ADMINRESTRICT_DENIED_MSG = "Unable To Access Admin From This IP Address"
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
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_REDIRECT_URL = "/dashboard"
LOGIN_URL = "/login"
LOGOUT_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "NettCare - Nett Hands Home Care - Caregiver Portal - "
# !SECTION

# SECTION - Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# !SECTION

# SECTION - STORAGE
# SECTION - StaticFiles Storage Vars - BunnyCDN
BUNNY_USERNAME = os.environ["BUNNY_USERNAME"]
BUNNY_PASSWORD = os.environ["BUNNY_PASSWORD"]
BUNNY_REGION = os.environ["BUNNY_REGION"]
BUNNY_HOSTNAME = os.environ["BUNNY_HOSTNAME"]
BUNNY_BASE_DIR = os.environ["BUNNY_BASE_DIR"]
# !SECTION
STORAGE_DESTINATION = os.environ["STORAGE_DESTINATION"]
FILE_UPLOAD_TEMP_DIR = os.environ["FILE_UPLOAD_TEMP_DIR"]


# SECTION - AWS settings
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
AWS_DEFAULT_ACL = "private"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_QUERYSTRING_EXPIRE = 3600
AWS_S3_REGION_NAME = "us-east-2"
AWS_CLOUDFRONT_KEY_ID = os.environ["AWS_CLOUDFRONT_KEY_ID"]
AWS_CLOUDFRONT_KEY = os.environ["AWS_CLOUDFRONT_PRIVATE_KEY"]
# !SECTION

# SECTION - S3 static settings
STATIC_LOCATION = "staticfiles/"
STATIC_URL = f"https://cdn.netthandshome.care/{STATIC_LOCATION}/"
STATIC_ROOT = STATIC_URL
# !SECTION

# SECTION -  S3 public media settings
PUBLIC_MEDIA_LOCATION = "media/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
# !SECTION

# SECTION - S3 private media settings
PRIVATE_MEDIA_LOCATION = "restricted/"
MEDIA_DIRECTORY = "/restricted/compliance/"
PRIVATE_FILE_STORAGE = "nhhc.backends.storage_backends.PrivateMediaStorage"
PRIVATE_MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PRIVATE_MEDIA_LOCATION}/"

# !SECTION
# SECTION - File Management
ALLOWED_UPLOAD_MIME_TYPES = list(os.environ["ALLOWED_MIME_TYPES"].split(","))
STORAGES = {
    "default": {"BACKEND": "nhhc.backends.storage_backends.PrivateMediaStorage"},
    "staticfiles": {
        "BACKEND": "nhhc.backends.storage_backends.StaticStorage",
    },
}

WHITENOISE_MANIFEST_STRICT = False
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


# SECTION -  Static files (CSS, JavaScript, Images, Templates)

# SECTION - Staticfile Dirs
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
    os.path.join(BASE_DIR, "static", "vendor"),
]
# !SECTION

# SECTION - Templates
TEMPLATE_DIR = [
    os.path.join(BASE_DIR, "templates"),
    os.path.join(BASE_DIR, "web", "templates"),
    os.path.join(BASE_DIR, "employee", "templates"),
    os.path.join(BASE_DIR, "authentication", "templates"),
    os.path.join(BASE_DIR, "portal", "templates"),
    os.path.join(BASE_DIR, "compliance", "templates"),
    os.path.join(BASE_DIR, "announcements", "templates"),
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": TEMPLATE_DIR,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "nhhc.utils.context_processors.from_settings",
            ],
        },
    },
]
# !SECTION

# !SECTION

# SECTION - Logging
LOGGING_CONFIG = None
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <magenta>{name}</magenta>:<cyan>Function: {function}</cyan>:<white>File: {file}</white>:<blue> Line: {line}</blue> - <level>{message}</level>'"

HIGHLIGHT_MOINITORING = highlight_io.H(
    "jdkmrpog",
    integrations=[DjangoIntegration()],
    instrument_logging=True,
    service_name="netthands-app",
    service_version="git-sha",
    environment=str(os.environ["HIGHLIGHT_ENV"]),
)
PRIMARY_LOG_FILE = os.path.join(os.environ.get("LOG_FILE_DIRECTORY"), "primary_ops.log")
CRITICAL_LOG_FILE = os.path.join(os.environ.get("LOG_FILE_DIRECTORY"), "fatal.log")
DEBUG_LOG_FILE = os.path.join(os.environ.get("LOG_FILE_DIRECTORY"), "debug.log")
LOGTAIL_HANDLER = LogtailHandler(source_token=os.environ["LOGTAIL_API_KEY"])
DEFAULT_HANDLER = sys.stdout
logger.add(
    HIGHLIGHT_MOINITORING.logging_handler,
    format=LOG_FORMAT,
    level="DEBUG",
    backtrace=True,
    serialize=True,
)
logger.add(DEBUG_LOG_FILE, format=LOG_FORMAT, colorize=True, diagnose=True, catch=True, backtrace=True, level="DEBUG")
logger.add(PRIMARY_LOG_FILE, colorize=True, format=LOG_FORMAT, diagnose=False, catch=True, backtrace=False, level="INFO")
logger.add(LOGTAIL_HANDLER, colorize=True, format=LOG_FORMAT, diagnose=False, catch=True, backtrace=True, level="DEBUG")
logger.add(DEFAULT_HANDLER, colorize=True, format=LOG_FORMAT, diagnose=True, catch=True, backtrace=True, level="DEBUG")
REQUEST_LOG_USER = True
REQUEST_TRAFFIC_MODULES = [
    "request.traffic.UniqueVisitor",
    "request.traffic.UniqueVisit",
    "request.traffic.Hit",
    "request.traffic.Search",
    "request.traffic.User",
    "request.traffic.Error404",
    "request.traffic.Error",
]
# !SECTION

# SECTION - Preformence Monitoring

PROMETHEUS_LATENCY_BUCKETS = (
    0.1,
    0.2,
    0.5,
    0.6,
    0.8,
    1.0,
    2.0,
    3.0,
    4.0,
    5.0,
    6.0,
    7.5,
    9.0,
    12.0,
    15.0,
    20.0,
    30.0,
    float("inf"),
)
PROMETHEUS_METRIC_NAMESPACE = "care_nett"
# !SECTION

# SECTION  - REST API CONFIGURATIONS
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ]
}
# !SECTION

if not TESTING:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        "debug_toolbar",
        "mail_panel",
    ]
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
    "mail_panel.panels.MailToolbarPanel",
]
# SECTION - ADMIN Backend
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "NettCare Control Center",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Control Center",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Control Center",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/logo-light.png",
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": "img/logo-dark.png",
    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,
    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "img/favicon.png",
    # Welcome text on the login screen
    "welcome_sign": "Welcome to the NettCare Control Center",
    # Copyright on the footer
    "copyright": "Blackberry Py, LLC",
    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    "search_model": ["employee.Employee", "auth.Group", "web.interested"],
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # model admin to link to (Permissions checked against model)
        {"model": "employee.Employee"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {
            "name": "Support",
            "url": "https://github.com/NettHandsHomeCare-Portal/NettHands/issues",
            "new_window": True,
        },
        {"model": "employee.Employee"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": ["sites", "robots"],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # Custom links to append to app groups, keyed on app name
    "order_with_respect_to": [""],
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gall2ery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fa-solid fa-users-gear",
        "employee.Employee": "fas fa-user",
        "auth.Group": "fa-solid fa-users-gear",
        "compliance.Contract": "fa-solid fa-file-contract",
        "rest_framework.authtoken.Token": "fa-solid fa-certificate",
        "authentication.UserProfile": "fa-solid fa-id-badge",
        "compliance.Compliance": "fa-solid fa-scale-balanced",
        "web.EmploymentApplicationModel": "fa-solid fa-file-circle-plus",
        "web.ClientInterestSubmission": "fa-solid fa-person-circle-plus",
        "portal.PayrollException": "fa-solid fa-money-bill",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Add a language dropdown into the admin
    "language_chooser": False,
}
# !SECTION
# SECTION - ASYNC/BACKGROUND WORKERS
CELERY_BROKER_URL = os.environ["ASYNC_QUEUE_BROKER_URI"]
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = os.environ["CELERY_TRACK_TASK_START"]
CELERY_TASK_TIME_LIMIT = int(os.environ["CELERY_TASK_TIME_LIMIT"]) * 60
CELERY_RESULT_BACKEND = "django-db"
CELERY_CACHE_BACKEND = "celery"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_RESULT_EXTENDED = True

# !SECTION
