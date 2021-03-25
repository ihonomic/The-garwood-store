from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Import models
from .models import *

# Create your views here.
from random import randrange

# initializing a value
value = 7


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
    #     # Querying all the products from the database
    products = Product.objects.all()

    #   Lets randomly generate 'fake' viewed & top-rated products - (Of course this section is incorect but it works for now)
    #   This changes the viewed & top rated products on-reload

    y = randrange(value)
    x = randrange(value)
    recentlyViewed = Product.objects.all()[x:y]

    a = randrange(value)
    b = randrange(value)
    topRated = Product.objects.all()[a:b]

    context = {"products": products,
               'recentlyViewed': recentlyViewed, 'topRated': topRated}
    return render(request, 'account/products.html', context)


def DetailProduct(request, slug):

    product = Product.objects.get(slug=slug)

    similarProduct = Product.objects.filter(
        category__icontains=product.category)

    context = {'product': product, 'similarProduct': similarProduct}
    return render(request, 'account/product-detail.html', context)
