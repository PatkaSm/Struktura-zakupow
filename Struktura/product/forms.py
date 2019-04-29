from django import forms
from django.contrib.auth.models import User
from cart.models import Cart
from product.models import Product


Category=((1, 'Owoce'), (2, 'Warzywa'), (3, 'Mięso'), (4, 'Alkohol'), (5, 'Woda'), (6, 'Napoje słodkie'),
          (7, 'Przekąski słone'), (8, 'Słodycze'), (9, 'Elektronika'), (10, 'Akcesoria domowe'), (11, 'Usługi'), (12, 'Rozrywka'))

class NewProductForm(forms.ModelForm):
    name = forms.CharField(label="Nazwa produkt")
    price = forms.DecimalField(label=('Cena'))
    category = forms.ChoiceField(widget=forms.Select(), choices=Category, label='Kategoria')
    cart = forms.ModelChoiceField(required=True, queryset=Cart.objects.filter()) # dodać request.user


    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'cart']