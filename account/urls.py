from django.contrib import admin
from django.urls import path
from . import views

""" WARNING:  URLs with .as_view() method are CBV """

urlpatterns = [

    path('login', views.Login, name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.logoutUser, name='logout'),

    path('', views.Home.as_view(), name='Home'),
    path('store/', views.ProductStore, name='store'),
    path('store/<slug:slug>',
         views.ProductDetailView.as_view(), name='DetailProduct'),

    path('account/', views.AccountPage.as_view(), name='account'),
    path('wishlist/', views.WishListPage.as_view(), name='wishlist'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),

    path('contact-us/', views.ContactUs.as_view(), name='contact-us'),
    path('blog/', views.Blog.as_view(), name='blog'),




]
