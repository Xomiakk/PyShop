from django import views
from django.urls import re_path
from orders import views

urlpatterns = [
    re_path(r'^order/$', views.order, name='order'),
]