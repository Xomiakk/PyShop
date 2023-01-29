from django.shortcuts import render
from products.models import *

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    return render(request, 'homepage/home.html', locals())
