"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home
    url(r'^$', views.index, name = 'index'),

    # Show all topics
    url(r'^topics/$', views.topics, name = 'topics'),
]