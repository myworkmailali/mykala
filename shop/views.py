from pyexpat.errors import messages

from django.shortcuts import render,redirect

import cart.cart
from .forms import SignupForm,ChangeProfileForm,ChangePasswordForm,UserInfoForm
from .models import Product, Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Profile
import json

from payment.forms import  ShippingAddressForm
from payment.models import ShippingAddress

from cart.cart import Cart
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
            current_user=Profile.objects.get(user__id=user.id)
            db_cart=current_user.old_cart
            if db_cart:
                db_cart=json.loads(db_cart)
                cart=Cart(request)
                for key,val in db_cart.items():
                    cart.db_add(key,val)



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

def update_profile(request):

    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        user_form = ChangeProfileForm(request.POST or None,instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(request,'پروفایل شما ویرایش شد')
            return redirect('home')
        return render(request, 'update_profile.html', {'form': user_form})

    else:
        messages.success(request,'مشکلی در ویرایش پروفایل وجود دارد')
        return redirect('home')

def user_info(request):
    if request.user.is_authenticated:
        current_user=Profile.objects.get(user__id=request.user.id)
        current_shipping_user=ShippingAddress.objects.get(user__id=request.user.id)
        user_form = UserInfoForm(request.POST or None, instance=current_user)
        shipping_form=ShippingAddressForm(request.POST or None,instance=current_shipping_user)
        if user_form.is_valid() or shipping_form.is_valid():
            user_form.save()
            shipping_form.save()

            messages.success(request, 'اطلاعات کاربری شما ویرایش شد')
            return redirect('home')
        return render(request, 'user_info.html', {'form': user_form,'shipping_form':shipping_form})

    else:
        messages.success(request, 'مشکلی در ویرایش اطلاعات کاربری شما وجود دارد')
        return redirect('home')

def update_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method == "POST":
            form=ChangePasswordForm(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'کلمه عبور شما با موفقیت تغییر یافت')
                login(request,current_user)
                return redirect('profile')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('profile')
        else:
            form=ChangePasswordForm(current_user)
            return render(request,'update_password.html',{'form':form})

    else:
        messages.success(request,'اول باید لاگین شوید')
        return redirect('home')




def product(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'product.html',{'product':product})

def category(request,cat):
    cat=cat.replace('-',' ')
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})
    except:
        messages.success(request,'دسته بندی مورد نظر یافت نشد')
        return redirect('home')

def category_summary(request):
    allcats=Category.objects.all()
    return render(request,'category_summary.html',{'allcats':allcats})

def search(request):
    if request.method == "POST":
        searched=request.POST.get('searched')
        if(searched):
            searched=Product.objects.filter(Q(name__icontains=searched)|Q(description__icontains=searched))
            if searched:
                return render(request, 'search.html', {'searched': searched})

    return render(request,'search.html',{})

