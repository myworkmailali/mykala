from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام خود را وارید کنید',
        })
    )

    last_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام خانوادگی خود را وارید کنید',
        })
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'ایمیل خود را وارد کنید'
        })

    )
    username = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'نام کاربری خود را وارد کنید'
        })
    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'name':'password1',
            'type': 'password',
            'placeholder':'کلمه عبور خود را وارد کنید',
        })
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'name':'password2',
            'type': 'password',
            'placeholder':'دوباره کلمه عبور خود را وارد کنید',
        })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
