from django.conf import settings
from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    brand_country = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name

class Car(models.Model):
    car_name = models.CharField(max_length=200)
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name
