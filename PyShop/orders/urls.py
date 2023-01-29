from django import views
from django.urls import re_path
from orders import views

urlpatterns = [
	re_path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    re_path(r'^basket/$', views.basket, name='basket'),
	re_path(r'^payment/$', views.payment, name='payment'),
]