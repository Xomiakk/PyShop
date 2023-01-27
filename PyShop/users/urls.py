from django import views
from django.urls import path, re_path
from django.views.generic import TemplateView
from users import views


urlpatterns = [
	# path("", TemplateView.as_view(template_name="homepage/home.html"), name="home"),
	  re_path(r'^$', views.home, name='home'),
]
