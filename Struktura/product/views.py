from django.shortcuts import render

# Create your views here.
from cart.models import Cart


def show_products(request):
    data = Cart.objects.filter(user=request.user)
    return render(request, "Cart.html", {'data': data})