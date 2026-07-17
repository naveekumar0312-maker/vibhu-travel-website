from pathlib import Path

# ==========================================
# BASE DIRECTORY
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================
# SECURITY
# ==========================================

SECRET_KEY = "django-insecure-change-this-key"

DEBUG = True

ALLOWED_HOSTS = []

# ==========================================
# INSTALLED APPS
# ==========================================

INSTALLED_APPS = [

    # Jazzmin
    "jazzmin",

    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local Apps
    "website",

]

# ==========================================
# MIDDLEWARE
# ==========================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==========================================
# ROOT URL
# ==========================================

ROOT_URLCONF = "travel.urls"

# ==========================================
# TEMPLATES
# ==========================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==========================================
# WSGI
# ==========================================

WSGI_APPLICATION = "travel.wsgi.application"

# ==========================================
# DATABASE (MYSQL)
# ==========================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "travel_db",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}

# ==========================================
# PASSWORD VALIDATION
# ==========================================

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

# ==========================================
# LANGUAGE
# ==========================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = False

# ==========================================
# STATIC FILES
# ==========================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# ==========================================
# MEDIA FILES
# ==========================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# ==========================================
# DEFAULT PRIMARY KEY
# ==========================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==========================================
# JAZZMIN ADMIN SETTINGS
# ==========================================

# ==========================================
# JAZZMIN PREMIUM SETTINGS
# ==========================================

JAZZMIN_SETTINGS = {

    # --------------------------------------------------
    # GENERAL
    # --------------------------------------------------

    "site_title": "Vibhu Travel Hub",

    "site_header": "Vibhu Travel Hub",

    "site_brand": "Vibhu Travel Hub",

    "site_logo": "images/logo/logo.JPG.jpeg",

    "login_logo": "images/logo/logo.JPG.jpeg",

    "login_logo_dark": "images/logo/logo.JPG.jpeg",

    "site_logo_classes": "img-circle",

    "welcome_sign": "Welcome to Vibhu Travel Hub Administration",

    "copyright": "© 2026 Vibhu Travel Hub",

    "site_icon": "images/favicon.ico",

    # --------------------------------------------------
    # UI
    # --------------------------------------------------

    "show_sidebar": True,

    "navigation_expanded": True,

    "hide_apps": [],

    "hide_models": [],

    "show_ui_builder": True,

    "changeform_format": "horizontal_tabs",

    "related_modal_active": True,

    "language_chooser": False,

    # --------------------------------------------------
    # SEARCH
    # --------------------------------------------------

    "search_model": [

        "website.Vehicle",

        "website.Enquiry",

        "auth.User",

    ],

    # --------------------------------------------------
    # TOP MENU
    # --------------------------------------------------

    "topmenu_links": [

        {

            "name": "Dashboard",

            "url": "admin:index",

            "permissions": ["auth.view_user"]

        },

        {

            "model": "website.Vehicle"

        },

        {

            "model": "website.Enquiry"

        },

        {

            "app": "website"

        },

    ],

    # --------------------------------------------------
    # SIDE MENU ORDER
    # --------------------------------------------------

    "order_with_respect_to": [

        "website",

        "auth",

    ],

    # --------------------------------------------------
    # ICONS
    # --------------------------------------------------

    "icons": {

        "auth": "fas fa-users-cog",

        "auth.user": "fas fa-user",

        "auth.Group": "fas fa-users",

        "website.Vehicle": "fas fa-bus",

        "website.Enquiry": "fas fa-phone-volume",

    },

    "default_icon_parents": "fas fa-folder",

    "default_icon_children": "fas fa-circle",

    # --------------------------------------------------
    # BUTTONS
    # --------------------------------------------------

    "actions_sticky_top": True,

}

JAZZMIN_UI_TWEAKS = {

    "theme": "darkly",

    "dark_mode_theme": "darkly",

    "navbar": "navbar-dark navbar-danger",

    "accent": "accent-danger",

    "navbar_small_text": False,

    "footer_small_text": False,

    "body_small_text": False,

    "brand_small_text": False,

    "sidebar_nav_small_text": False,

    "sidebar_disable_expand": False,

    "sidebar_nav_child_indent": True,

    "sidebar_nav_compact_style": False,

    "sidebar_nav_legacy_style": False,

    "sidebar_nav_flat_style": False,

    "theme_colour": "navbar-danger",

    "button_classes": {

        "primary": "btn-danger",

        "secondary": "btn-dark",

        "info": "btn-info",

        "warning": "btn-warning",

        "danger": "btn-danger",

        "success": "btn-success"

    }

}