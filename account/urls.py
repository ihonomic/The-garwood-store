from django.contrib import admin
from django.urls import path
from . import views
from account.views import ProductDetailView

urlpatterns = [
    path('login', views.loginpage, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutUser, name='logout'),

    path('', views.Home, name='Home'),
    path('store/', views.ProductStore, name='store'),
    path('store/<slug:slug>',
         views.ProductDetailView.as_view(), name='DetailProduct'),


]
