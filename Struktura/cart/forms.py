from django import forms
from cart.models import Cart


class NewCartForm(forms.ModelForm):
    cart_name = forms.CharField(max_length=100, label=(""))

    class Meta:
        model = Cart
        fields = ['cart_name']