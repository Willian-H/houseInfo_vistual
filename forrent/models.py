from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class forrent(models.Model):
    houseaddress = models.CharField(max_length=255)
    houseprice = models.CharField(max_length=255)
    housearea = models.CharField(max_length=255)
    housedescription = models.CharField(max_length=255)
    linkman = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
