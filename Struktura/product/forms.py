from django import forms
from product.models import Product, Category


class NewProductForm(forms.ModelForm):
    name = forms.CharField(label=("Nazwa produkt"))
    price = forms.DecimalField
    product = forms.ChoiceField(widget=forms.Select(), oices=Category)

    class Meta:
        model = Product
        fields = ['name', 'price', 'product']