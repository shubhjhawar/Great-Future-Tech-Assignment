from django.db import models

# Create your models here.

class DataModel(models.Model):
    ProductName = models.CharField(max_length=200)
    ProductID = models.IntegerField()
    ProductQuantity = models.IntegerField()
