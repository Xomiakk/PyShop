from django.shortcuts import render
from orders.models import *

def order(request):
    
    return render(request, 'order/order.html', locals())