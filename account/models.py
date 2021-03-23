from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    # this user attribute links the django user default model user - since we are going to be inheriting from it
    # CASCADE- means django should delete this Customer and anything associated with it when the user is deleted
    user = models.OneToOneField(User, null=True, blank=True,
                                on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    sold_out = models.BooleanField(default=False)
    description = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    img = models.ImageField(blank=True, null=True, default="profile_pic.png")

    def __str__(self):
        return self.name

    # We will query our image field with this function, to catch errors when an image is deleted
    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url


class Order(models.Model):
    # creating drop down menu in status selection

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    othername = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.address