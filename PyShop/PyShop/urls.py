from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("users/", include("users.urls")),
    path("accounts/", include("allauth.urls")),
	path("products/", include("products.urls")),
	path("orders/", include("orders.urls")),
]
