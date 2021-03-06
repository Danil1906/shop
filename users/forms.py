from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from phonenumber_field.formfields import PhoneNumberField


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    phone = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-control'}),

                             label="Номер телефона", required=True)

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class PromoForm(forms.Form):
    promo = forms.CharField(label='Промокод', required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'необязательно поле'
    }))
