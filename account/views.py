from django.shortcuts import render, redirect
from django.http import HttpResponse


#from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView

from random import randrange
# initializing a value
value = 7


from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .forms import CreateUserFrom
from .models import *
from .decorators import unauthenticated_user, allowed_users, admin_only

from .filters import ProductFilter

#hit counts helps count the numberof times a page was visited
from hitcount.views import HitCountDetailView




# Create your views here.


@unauthenticated_user
def register(request):

    form = CreateUserFrom()
    if request.method == 'POST' :
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                full_name=user.username,
                email=user.email,
            )

            messages.success(request, 'Account was created ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)



@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'Welcome to Garwood...')
            return redirect('store')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('store')



def Home(request):
    return render(request, 'account/home.html')

def AboutGarwood(request):
    context = {}
    return render(request, 'account/home.html', context)


def ProductStore(request):
    # Querying all the products from the database
    products = Product.objects.all().order_by('-date_created')
    query = request.GET.get("q")  # another example of search/filter query
    if query:
        products = products.filter(name__icontains=query)

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

#we need to use a class based view to get the hit count, this was the only
# method i could get at the time
class ProductDetailView(HitCountDetailView):
    model = Product
    template_name = 'account/product-detail.html'
    slug_field = "slug"
    count_hit = True


def DetailProduct(request, slug):


    product = Product.objects.get(slug=slug)


    similarProduct = Product.objects.filter(
        category__icontains=product.category)

    context = {'product': product, 'similarProduct': similarProduct}
    return render(request, 'account/product-detail.html', context)
