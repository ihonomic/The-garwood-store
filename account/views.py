from django.shortcuts import render
from django.http import HttpResponse

# Import models
from .models import Product

# Create your views here.

def Home(request):
    context = {}
    return render(request, 'account/home.html', context)

def Login(request):
    context = {}
    return render(request, 'account/home.html', context)

def Register(request):
    context = {}
    return render(request, 'account/home.html', context)

def AboutGarwood(request):
    context = {}
    return render(request, 'account/home.html', context)


def ProductStore(request):
    # Querying all the products from the database
    products = Product.objects.all()

    context = {"products":products}
    return render(request, 'account/products.html', context)
