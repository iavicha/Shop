from django.db import models
from django.contrib.auth.models import User as UserAuth


# Create your models here.


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)


class Product(models.Model):
    TYPE = (
        ('fruits', 'fruits'),
        ('vegetables', 'vegetables')
    )
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount_price = models.FloatField()
    discount = models.IntegerField()

    type = models.CharField(max_length=10, choices=TYPE)


class Coupon(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    value = models.IntegerField()
    min_coast = models.IntegerField()
    starts = models.DateTimeField()
    ends = models.DateTimeField()


class Cart(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together = (('user', 'product'),)
