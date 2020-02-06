"""Defines URL patterns for users"""

from django.conf.urls import url
from django.contrib.auth import login
from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
]