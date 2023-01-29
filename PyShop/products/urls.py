from django.urls import re_path
from django.contrib import admin
from products import views

urlpatterns = [
   
    re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]