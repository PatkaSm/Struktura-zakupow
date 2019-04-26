from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

from cart.forms import NewCartForm
from cart.models import Cart


def index(request):
    return render(request, "newCart.html")


def new_cart_view(request):
    if request.method == 'POST':
        form = NewCartForm(request.POST or None)
        if form.is_valid():
            cart = form.save(commit = False)
            cart.user = request.user
            cart.date_added = timezone.now()
            cart.save()
            cart_name = form.cleaned_data.get('cart_name')
            messages.success(request, 'Koszyk {cart_name} został utworzony! Dodaj do niego produkty.'.format(cart_name=cart_name))
            return redirect('cart')
    else:
        form = NewCartForm()
    return render(request, "newCart.html", {'form': form})


def show_cart(request):
    data = Cart.objects.filter()
    return render(request, "cart_structure.html", {'data' : data})


def show_products(request):
    data = Cart.objects.filter()
    print(data)
    return render(request, "index.html", {'data' : data})


