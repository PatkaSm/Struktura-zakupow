from django import forms
from cart.models import Cart
from product.models import Product, Category


class NewProductForm(forms.ModelForm):
    name = forms.CharField(label="Nazwa produkt")
    price = forms.DecimalField(label=('Cena'))
    category = forms.ChoiceField(widget=forms.Select(), choices=Category, label='Kategoria')

    def __init__(self,  *args, user, **kwargs):
        super(NewProductForm, self).__init__(*args, **kwargs)
        self.fields['cart'] = forms.ModelChoiceField(queryset=Cart.objects.filter(user=user), label="Koszyk")

    class Meta:
        model = Product
        fields = ['name', 'price', 'category']


class selectCart(forms.Form):

    def __init__(self, *args, user, **kwargs):
        super(selectCart, self).__init__(*args, **kwargs)
        self.fields['cart'] = forms.ModelChoiceField(queryset=Cart.objects.filter(user=user), label="Koszyk")

