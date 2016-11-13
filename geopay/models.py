from django.db import models

class Customer(models.Model):
    cust_id = models.CharField(max_length=256)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=20)

class Merchant(models.Model):
    merchant_id = models.CharField(max_length=30)
    longitude = models.DecimalField(decimal_places=5, max_digits=10)
    latitude = models.DecimalField(decimal_places=5, max_digits=10)
    products = models.ManyToManyField(Products)
