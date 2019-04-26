from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
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
            messages.success(request, 'Produkt  {name} został utworzony i dodany do koszyka!'.format(name=name))
            return redirect('cart')
    else:
        form = NewProductForm()
    return render(request, "cart.html", {'form': form})
