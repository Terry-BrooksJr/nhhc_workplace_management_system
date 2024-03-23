"""
Module: urls.py
Description: This module contains the URL patterns for the frontend application.
"""

from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from web import views
urlpatterns = [
    path("", csrf_exempt(views.index), name="index"),
    path("about/", views.about, name="about"),
    path("client-interest/", views.client_interest, name="client-interest"),
    path("employment-application/", views.employee_interest, name="application"),
    path("submission-confirmation/", views.submitted, name="submitted"),
    re_path(r"^favicon/$", views.favicon, name="favicon")
]
