# models.py in your app directory (e.g., products)

from django.db import models

class ProductMaster(models.Model):
    created_at = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    asin = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.asin

class ProductUpdateHistory(models.Model):
    product = models.ForeignKey(ProductMaster, on_delete=models.CASCADE)
    created_at = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255)
    asin = models.CharField(max_length=20)
    previous_attribute = models.CharField(max_length=255)
    current_attribute = models.CharField(max_length=255)

class Job(models.Model):
    name = models.CharField(max_length=255)
    total_count = models.IntegerField(default=0)
    current_count = models.IntegerField(default=0)
    created_at = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255)
