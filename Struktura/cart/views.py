from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from cart.forms import NewCartForm
from cart.models import Cart
from product.forms import selectCart
from django.db.models import Sum, Count
import json
from django.core.serializers.json import DjangoJSONEncoder


@login_required(login_url="/")
def index(request):
    return render(request, "newCart.html")


@login_required(login_url="/")
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
        elif 'deleteButton' in request.POST:
            delete_cart = Cart.objects.filter(id=request.POST['cart_id'])
            print(delete_cart)
            if delete_cart.exists():
                cart = Cart.objects.get(id=delete_cart[0].id)
                delete_cart.delete()
                messages.success(request, 'Koszyk {name} został usunięty!'.format(name=cart))
                all_carts = Cart.objects.filter(user=request.user)
                form = NewCartForm()
                return render(request, "newCart.html",
                              {'carts': all_carts,'form': form})

    else:
        form = NewCartForm()
        all_carts = Cart.objects.filter(user=request.user)

    return render(request, "newCart.html", {'form': form, 'carts':all_carts})


@login_required(login_url="/")
def show_cart(request):
    if request.method == 'POST':
        form2 = selectCart(request.POST, user=request.user)
        if form2.is_valid():
            cart = form2.cleaned_data.get('cart')
            cart_from_form = Cart.objects.get(id=cart.id)
            products = cart_from_form.product.filter(user=request.user)
            sum_product_price_by_category = products.values('category').annotate(total = Count('id'), total_price = Sum('price')).order_by('category')
            sum_products =Cart.objects.filter(id = cart.id, user = request.user).aggregate(Sum('product__price'))['product__price__sum']
            dane = products.values('category').annotate(total_price = Sum('price'))
            #danejson = json.dumps(list(dane), cls=DjangoJSONEncoder)
            return render(request, "cart_structure.html", {'form':form2,'products':sum_product_price_by_category, 'sum_products': sum_products,})
    else:
        form2 = selectCart(user=request.user)
    return render(request, "cart_structure.html", {'form':form2,})






