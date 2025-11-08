from pyexpat.errors import messages

from django.shortcuts import render,redirect

from .forms import SignupForm
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from . import forms



def index(request):
    all_products = Product.objects.all()
    return render(request,'index.html',{'products':all_products})

def about(request):
    return render(request,'about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'شما با موفقیت وارد سامانه شدید')
            return redirect('home')
        else:
            messages.error(request, 'نام کاربری یا کلمه عبور نادرست است')
    return render(request,'login.html' )

def logout_user(request):
    logout(request)
    messages.success(request,'شما با موفقیت از سامانه خارج شدید')
    return redirect('home')


def signup_user(request):
    form=SignupForm()
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')

            user = authenticate(request,username=username,password=password1)
            login(request,user)
            messages.success(request,'اکانت شما ساخته شد')
            return redirect('home')
        else:
            messages.success(request,'مشکلی در ثبت نام وجود دارد')
            return render('signup')
    else:
        return render(request, 'signup.html',{'form':form})
