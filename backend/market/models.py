from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, null='name-product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expiration_date = models.DateField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='static/images/covers/%Y/%m/%d/', null=True, blank=True)