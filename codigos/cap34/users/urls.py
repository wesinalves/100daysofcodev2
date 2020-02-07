"""Defines URL patterns for users"""

from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    path("login/", auth_views.LoginView.as_view(), name='login'),
]