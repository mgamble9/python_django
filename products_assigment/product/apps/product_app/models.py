from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=42)
    description = models.TextField(max_length=100)
    weight = models.CharField(max_length=42)
    price = models.CharField(max_length=42)
    cost = models.CharField(max_length=42)
    category = models.CharField(max_length=42)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
