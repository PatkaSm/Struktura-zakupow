from django.contrib.auth.models import User
from django.db import models
from product.models import Product


class Cart(models.Model):
    cart_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ManyToManyField(Product,  blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cart_name

