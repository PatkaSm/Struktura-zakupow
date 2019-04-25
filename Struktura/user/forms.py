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

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password1   = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        email = self.cleaned_data.get('email')
        username_qs = User.objects.filter(username=username)
        email_qs = User.objects.filter(email=email)
        if username_qs.exists():
            raise forms.ValidationError(
                "Ta nazwa użytkownika już istnieje")
        if password1 != password2:
            raise forms.ValidationError(
                "Podane hasła nie są takie same."
            )
        if email_qs.exists():
            raise forms.ValidationError(
                "Tn email został już użyty."
            )
        return super(UserRegisterForm, self).clean(*args, **kwargs)


