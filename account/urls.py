from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginpage, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutUser, name='logout'),

    path('', views.Home, name='Home'),
    path('store/', views.ProductStore, name='store')

]
