"""nhhc URL Configuration

The `urlpatterns` list routes URLs to views.
"""
import announcements.urls
import authentication.urls
import compliance.urls
import employee.urls
import portal.urls
import web.urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from loguru import logger
from web.sitemaps import StaticViewSitemap

sitemaps = {"static": StaticViewSitemap}
from django.http import HttpResponse

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("control-center/", admin.site.urls),
    re_path(r"^compliance/", include("filer.urls")),
    re_path(r"^", include("filer.server.urls")),
    path("", include(web.urls)),
    path("", include("allauth.urls")),
    re_path(
        r"^status/DNzaNdlwIbqjWCq4vMTAgGe81VxXFd1QPGt-mglUDuA/",
        include("health_check.urls"),
    ),
    # path("", include(authentication.urls)),
    path("", include(portal.urls)),
    path("", include(employee.urls)),
    re_path(r"^s3direct/", include("s3direct.urls")),
    path("", include(compliance.urls)),
    path("", include(announcements.urls)),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path(
        "robots.txt/",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    re_path("", include("django_prometheus.urls")),
    # path("404/", web.views.handler404),
    # path("500/", web.views.handler500)
]
HEALTH_CHECK = {
    "DISK_USAGE_MAX": 90,  # percent
    "MEMORY_MIN": 100,  # in MB
}
handler404 = web.views.handler404
handler500 = web.views.handler500
