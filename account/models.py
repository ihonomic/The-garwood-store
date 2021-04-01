from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
<<<<<<< HEAD


from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
=======
>>>>>>> 31b47a0d409794c0383713ce53da175585857268


# Create your models here.

class Customer(models.Model):
    # this user attribute links the django user default model user - since we are going to be inheriting from it
    # CASCADE- means django should delete this Customer and anything associated with it when the user is deleted
    user = models.OneToOneField(User, null=True, blank=True,
                                on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.full_name)


class Product(models.Model):
    product_type = (
        ('shirt', 'shirt'),
        ('toy', 'toy'),
        ('short', 'short'),
        ('necklace', 'necklace'),
        ('cap', 'cap'),
        ('unisex', 'unisex'),
        ('wristwatches', 'wristwatches'),
        ('nightgowns', 'nightgowns'),
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    discount_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    sold_out = models.BooleanField(default=False)
    description = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    img = models.ImageField(blank=True, null=True, default="profile_pic.png")
    category = models.CharField(
        max_length=20, null=True, blank=True, choices=product_type)
    slug = models.SlugField(null=True)
<<<<<<< HEAD
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
=======

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

>>>>>>> 31b47a0d409794c0383713ce53da175585857268
      # We will query our image field with this function, to catch errors when an image is deleted

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url

    def availabilty(self):
        if self.sold_out == False:
            available = 'In stock'
        else:
            available = 'Sold out'
        return available

<<<<<<< HEAD
=======
    def __str__(self):
        return self.name

>>>>>>> 31b47a0d409794c0383713ce53da175585857268

class Order(models.Model):
    # creating drop down menu in status selection

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(
        max_length=200, null=True, choices=STATUS, blank=True)
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
