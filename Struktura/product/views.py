from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from cart.models import Cart
from product.forms import NewProductForm, selectCart
from product.models import Product

@login_required(login_url="/")
def new_product_view(request):
    form = NewProductForm(request.POST, user=request.user)
    form2 = selectCart(request.POST, user=request.user)
    if request.method == 'POST':
        if 'addProduct' in request.POST:
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.date_added = timezone.now()
                product.save()
                cart = form.cleaned_data.get('cart')
                cart.product.add(product)
                cart.save()
                name = form.cleaned_data.get('name')
                messages.success(request,'Produkt  {name} został utworzony i dodany do koszyka  {cart}!'.format(name=name, cart=cart))
                oneCart = Cart.objects.get(id=cart.id)
                all_products_in_cart = oneCart.product.all().order_by('-date_added')
                form = NewProductForm(user=request.user)
                return render(request, "cart.html", {'form2': form2, 'all_products_in_cart': all_products_in_cart, 'form': form})

        elif 'deleteButton' in request.POST:
            delete_product = Product.objects.filter(id=request.POST['product_id'], user=request.user)
            if delete_product.exists():
                cart = Cart.objects.get(product=delete_product[0])
                delete_product_name = delete_product[0]
                delete_product.delete()
                messages.success(request,'Produkt {name} został usunięty z koszyka  {cart}!'.format(name= delete_product_name, cart=cart))
                form = NewProductForm(user=request.user)
                form2 = selectCart(user=request.user)
                oneCart = Cart.objects.get(id=cart.id)
                all_products_in_cart = oneCart.product.all().order_by('-date_added')
                return render(request, "cart.html", {'form2': form2, 'all_products_in_cart': all_products_in_cart, 'form': form})

        if form2.is_valid():
            form = NewProductForm(user=request.user)
            cart = form2.cleaned_data.get('cart')
            oneCart = Cart.objects.get(id=cart.id)
            all_products_in_cart = oneCart.product.all().order_by('-date_added')
            print(all_products_in_cart)
            return render(request, "cart.html", {'form2': form2, 'all_products_in_cart': all_products_in_cart, 'form': form})

    else:
        form = NewProductForm(user=request.user)
        form2 = selectCart(user=request.user)
    return render(request, "cart.html", {'form': form, 'form2': form2})


