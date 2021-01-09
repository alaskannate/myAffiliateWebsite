from django.db import models

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=120) #max_length
    description = models.TextField(default="An un labeled product",blank=False, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100)
    summery     = models.TextField(default="Hello")

class AffiliateProduct(models.Model):
    title       = models.CharField(max_length=120) #max_length
    description = models.TextField(blank=False, null=True)
    keyword     = models.TextField()
    link        = models.TextField(blank=True, null=True)
    permission  = models.BooleanField(default=False)
