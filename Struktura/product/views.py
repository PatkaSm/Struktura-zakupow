from django.contrib import messages
from django.shortcuts import render, redirect
from cart.models import Cart
from product.forms import NewProductForm, selectCart


def new_product_view(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, user=request.user)
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
        form = NewProductForm(user=request.user)
        data = Cart.objects.order_by('-date_added').filter(user = request.user)
    return render(request, "cart.html", {'form': form, 'data':data})


def show_products_by_cart(request):
    if request.method == 'POST':
        form2 = selectCart(request.POST, user=request.user)
        if form2.is_valid():
            cart = form2.cleaned_data.get('cart')
            data = Cart.objects.order_by('-date_added').filter(user=request.user, cart_name=cart.cart_name)
            return render(request, "cart.html", {'form':form2, 'data' : data})
    else:
        form2 = selectCart(user=request.user)
        data = Cart.objects.filter(user = request.user)
    return render(request, "cart.html", {'form2':form2, 'data' : data})