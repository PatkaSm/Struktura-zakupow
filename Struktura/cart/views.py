from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from cart.forms import NewCartForm
from cart.models import Cart
from product.forms import selectCart, Category
from django.db.models import F, Sum, Count


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
    if request.method == 'POST':
        form2 = selectCart(request.POST, user=request.user)
        if form2.is_valid():
            cart = form2.cleaned_data.get('cart')
            cart = Cart.objects.get(id=cart.id)
            products = cart.product.filter(user=request.user)
            sum_product_price_by_category = products.values('category').annotate(Sum('price')).annotate(Count('id')).order_by('category')


            return render(request, "cart_structure.html", {'form':form2,'data':sum_product_price_by_category})
    else:
        form2 = selectCart(user=request.user)
    return render(request, "cart_structure.html", {'form':form2})






