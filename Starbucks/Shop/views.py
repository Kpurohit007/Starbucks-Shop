from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def order_view(request):
    products = Product.objects.all()  # Fetching all products from the database
    return render(request, 'order.html', {'products': products})
