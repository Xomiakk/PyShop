from django import views
from django.urls import re_path
from users import views



urlpatterns = [
	re_path(r'^$', views.home, name='home'),
]
