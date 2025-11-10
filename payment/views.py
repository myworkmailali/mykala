

from django.shortcuts import render,redirect
from cart.cart import Cart
from payment.forms import  ShippingAddressForm
from payment.models import ShippingAddress
from django.contrib import messages

def payment_success(request):
    return render(request,'payment/payment_success.html',{})

def checkout(request):
    cart = Cart(request)
    products = cart.get_products()
    quantities = cart.get_quantity()
    total_ordering = cart.get_total()
    shipping_form = ShippingAddressForm(request.POST or None)
    if request.user.is_authenticated:
        current_user=ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form=ShippingAddressForm(request.POST or None,instance=current_user)
    if shipping_form.is_valid():
        shipping_form.save()
        messages.success(request, 'آدرس ارسال محصول با موفقیت ثبت شد')
    return render(request,'payment/checkout.html',{'products': products, 'quantities': quantities, 'total_ordering': total_ordering,'shipping_form':shipping_form})
