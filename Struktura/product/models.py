from django.db import models
from django.contrib.auth.models import User
# Create your models here.


Category=(('Owoce', 'Owoce'), ('Warzywa','Warzywa'),('Nabiał', 'Nabiał'),('Produkty zbożowe', 'Produkty zbrożowe'), ('Tłuszcze i oleje','Tłuszcze i oleje'),('Mięso', 'Mięso'),
          ('Alkohol', 'Alkohol'), ('Woda', 'Woda'), ('Napoje Słodkie', 'Napoje słodkie'),('Przekaski Słone', 'Przekąski słone'), ('Cukier i śłodycze', 'Cukier i słodycze'),
          ('Elektronika', 'Elektronika'), ('Dom i ogród', 'Dom i ogród'),('Chemia, śreodki czystości','Chemia, środki czystośi'),('Zwierzęta','Zwierzęta'), ('Artykuły biurowe', 'Artykuły biurowe'),
          ('Usługi', 'Usługi'), ('Kultura i rozrywka', 'Kultura i rozrywka'),('Ubrania', 'Ubrania'),('Buty i dodatki', 'Buty i dodatki'),
          ('Uroda', 'Uroda'),('Zdrowie', 'Zdrowie'),('Dziecko','Dziecko'),('Motoryzacja', 'Motoryzacja'),('Pozostałe', 'Pozostałe'))

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    category = models.CharField(max_length=100, choices=Category, default='Nieokreślony')

    def __str__(self):
        return self.name