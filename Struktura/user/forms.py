from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Nazwa użytkownika")
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput,)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Wprowadź poprawne dane!')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20,label="Nazwa użytkownika",widget=forms.TextInput(attrs={"class": "username"}))
    password1 = forms.CharField(label=("Hasło"),strip=False,widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Potwierdź hasło"),widget=forms.PasswordInput,strip=False,help_text=(""))
    email = forms.EmailField(label='Adres e-mail')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','email')


