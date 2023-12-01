from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class ProductClass(models.Model):
    product_class = models.CharField(max_length=30)

    def __str__(self):
        return self.product_class


class Product(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    image = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def add_to_cart(self):
        return reverse('add', kwargs={'id': self.id})

    def remove(self):
        return reverse('remove', kwargs={'id': self.id})


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def remove_from_cart(self, product):
        cart_item = CartItem.objects.get(cart=self, product=product)
        cart_item.delete()


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def increase_quantity(self):
        self.quantity += 1
        self.save()

    def decrease_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.save()
        else:
            self.delete()


class UserAddress(models.Model):
    numeric = RegexValidator(r'^[0-9]*$')

    email = models.EmailField()
    phone = models.CharField(max_length=11, validators=[numeric])
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.email
    

class UserVisa(models.Model):
    numeric = RegexValidator(r'^[0-9]*$')

    name = models.CharField(max_length=20)
    cardnumber = models.CharField(max_length=20)
    expirationdate = models.CharField(max_length=5)
    securitycode = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class OrderInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    address = models.TextField()

    name = models.CharField(max_length=20)
    cardnumber = models.CharField(max_length=20)
    expirationdate = models.CharField(max_length=5)
    securitycode = models.CharField(max_length=3)

    products = models.TextField(null=True)

    def __str__(self):
        return self.name