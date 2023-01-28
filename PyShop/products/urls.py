from django import views
from django.urls import re_path
from products import views

urlpatterns = [
    re_path(r'^basket/$', views.basket, name='basket'),
]