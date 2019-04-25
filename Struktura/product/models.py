from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Category=((1, 'Owoce'), (2, 'Warzywa'), (3, 'Mięso'), (4, 'Alkohol'), (5, 'Woda'), (6, 'Napoje słodkie'),
          (7, 'Przekąski słone'), (8, 'Słodycze'), (9, 'Elektronika'), (10, 'Akcesoria domowe'), (11, 'Usługi'), (12, 'Rozrywka'))

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    caterogry = models.IntegerField(choices=Category, default=(13, 'Nieokreślony'))