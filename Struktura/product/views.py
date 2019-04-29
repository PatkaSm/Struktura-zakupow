from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from cart.models import Cart
from product.forms import NewProductForm


def new_product_view(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST or None)
        if form.is_valid():
            product = form.save(commit = False)
            product.user = request.user
            product.save()
            cart = form.cleaned_data.get('cart')
            cart.product.add(product)
            cart.save()
            name = form.cleaned_data.get('name')
            messages.success(request, 'Produkt  {name} został utworzony i dodany do koszyka  {cart}!'.format(name=name, cart = cart))
            return redirect('cart')
    else:
        form = NewProductForm()
    data = Cart.objects.filter(user = request.user)
    return render(request, "cart.html", {'form': form,'data': data})


