from django.shortcuts import render
from products.models import *

def basket(request):
    
    return render(request, 'basket/basket.html', locals())