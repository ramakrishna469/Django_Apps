from django.db import models
from django.contrib import auth

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    category = models.ForeignKey(Category)
    # user = models.ForeignKey(User)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-price']

class Basket(models.Model):
    user = models.ForeignKey(auth.models.User)
    pname = models.ForeignKey(Product)
    def __str__(self):
        return self.user.username +"_"+ self.pname.name

