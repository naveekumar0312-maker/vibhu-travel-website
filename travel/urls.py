from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap

# ==========================
# Sitemap Configuration
# ==========================

sitemaps = {
    "static": StaticViewSitemap,
}

# ==========================
# URL Patterns
# ==========================

urlpatterns = [

    # Django Admin
    path("admin/", admin.site.urls),

    # Website
    path("", include("website.urls")),

    # Dynamic Sitemap
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),

]

# ==========================
# Media Files
# ==========================

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )