from pyexpat.errors import messages

from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


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
