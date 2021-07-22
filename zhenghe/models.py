from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class SecondHouse(models.Model):
    housetitle = models.CharField(max_length=255)
    houseaddress = models.CharField(max_length=255)
    houseprice = models.CharField(max_length=255)
    housearea = models.CharField(max_length=255)
    housedescription = models.CharField(max_length=255)


class NewHouse(models.Model):
    housetitle = models.CharField(max_length=255)
    houseaddress = models.CharField(max_length=255)
    houseprice = models.CharField(max_length=255)
    housearea = models.CharField(max_length=255)
    housedescription = models.CharField(max_length=255)


class RentHouse(models.Model):
    housetitle = models.CharField(max_length=255)
    houseaddress = models.CharField(max_length=255)
    houseprice = models.CharField(max_length=255)
    housearea = models.CharField(max_length=255)
    housedescription = models.CharField(max_length=255)
