from django.urls import path

from . import views


urlpatterns = [
    path('human', views.humanize, name='human'),
]