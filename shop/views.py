from django.shortcuts import render
from .models import Product

def index(request):
    all_products = Product.objects.all()
    return render(request,'index.html',{'products':all_products})

def about(request):
    return render(request,'about.html')
