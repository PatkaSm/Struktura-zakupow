from django.contrib.auth.views import logout_then_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)


def logout_view(request):
    logout(request)
    return logout_then_login(request,login_url='/login')


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('newcart')
    return render(request, "login.html", {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, '{username} Twoje konto zostało założone, możesz się zalogować!'.format(username=username))
            return redirect('user_login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})