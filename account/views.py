""" CLASS BASE VIEWS IMPORTS """
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from hitcount.views import HitCountDetailView


from .filters import ProductFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

from .models import *
from .forms import CreateUserFrom
from django.contrib.auth.models import Group

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


from random import randrange


# Create your views here.

""" initializing a random value"""
value = 7


class RegisterView(FormView):
    # template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        user = form.save()
        # Login the user
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Registration Success')
        return super(RegisterView, self).form_valid(form)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(
                request, f"Welcome back {request.user}, Happy shopping...")
            return redirect('store')
        else:
            messages.info(request, 'Username or password is incorrect')
        return render(request, 'account/main.html')


def logoutUser(request):
    logout(request)
    return redirect('store')


class Home(TemplateView):
    template_name = 'account/home.html'


class AccountPage(TemplateView):
    template_name = 'account/account.html'


class WishListPage(TemplateView):
    template_name = 'account/wishlist.html'


class Cart(TemplateView):
    template_name = 'account/cart.html'


class Checkout(TemplateView):
    template_name = 'account/checkout.html'


class ContactUs(TemplateView):
    template_name = 'account/contact.html'


class Blog(TemplateView):
    template_name = 'account/blog.html'


def ProductStore(request):
    """  Querying all the products from the database """

    products = Product.objects.all().order_by('-date_created')

    """ Lets randomly generate 'fake' viewed & top-rated products - (Of course this section is incorect but it works for now)
    This changes the viewed & top rated products on-reload """
    y = randrange(value)
    x = randrange(value)
    recentlyViewed = Product.objects.all()[x:y]

    a = randrange(value)
    b = randrange(value)
    topRated = Product.objects.all()[a:b]

    context = {"products": products,
               'recentlyViewed': recentlyViewed, 'topRated': topRated}
    return render(request, 'account/products.html', context)


class ProductDetailView(HitCountDetailView):
    """  CBV to get the hit count, as it was the only method wisdom could get at the time - WISDOM"""

    model = Product
    template_name = 'account/product-detail.html'
    context_object_name = 'product'
    slug_field = "slug"
    count_hit = True

    def get_context_data(self, *args,  **kwargs):
        """ Modified wisdom hitcount idea to get similar products on the same page - IHON"""

        slug = self.kwargs['slug']
        product = Product.objects.get(slug=slug)

        context = super(ProductDetailView, self).get_context_data()
        context['similarProduct'] = Product.objects.filter(
            category__icontains=product.category)
        return context
