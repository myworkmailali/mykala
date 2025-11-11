from datetime import timezone

from django.shortcuts import render,redirect,get_object_or_404
from cart.cart import Cart
from payment.forms import  ShippingAddressForm
from payment.models import ShippingAddress
from django.contrib import messages
from shop.models import Profile
from .models import Order,OrderItems,Product
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
#    if shipping_form.is_valid():
#        shipping_form.save()
#        messages.success(request, 'آدرس ارسال محصول با موفقیت ثبت شد')
    return render(request,'payment/checkout.html',{'products': products, 'quantities': quantities, 'total_ordering': total_ordering,'shipping_form':shipping_form})


def order_confirm(request):
    cart = Cart(request)
    products = cart.get_products()
    quantities = cart.get_quantity()
    total_ordering = cart.get_total()
    shipping_info=request.POST
    request.session['shipping_info']=shipping_info
    if request.method == 'POST':
       pass
    else:
       messages.success(request,'شما دسترسی به این صفحه را ندارید')
       return redirect('home')
    return render(request,'payment/order_confirm.html',{'products': products, 'quantities': quantities, 'total_ordering': total_ordering,'shipping_info':shipping_info})

def order_process(request):
    if request.method == 'POST':
        shipping_info = request.session.get('shipping_info')
        address=shipping_info['shipping_address_address']
        city=shipping_info['shipping_address_city']
        state=shipping_info['shipping_address_state']
        country=shipping_info['shipping_address_country']
        zipcode=shipping_info['shipping_address_zipcode']

        cart = Cart(request)
        products = cart.get_products()
        quantities = cart.get_quantity()
        total_ordering = cart.get_total()

        full_name = shipping_info['shipping_address_full_name']
        shipping_address_full_name =f'{city}\n {state} \n{country}\n {zipcode}\n{address}'

        order_status = 'pending'
        if request.user.is_authenticated:
            shipping_user=request.user
            new_order = Order(
                user=shipping_user,
                order_status=order_status,
                shipping_address_full_name=shipping_address_full_name,
                amount_paid=total_ordering,
            )
            new_order.save()

            order_id = get_object_or_404(Order, pk=new_order.pk)
            for product in products:
                prod = get_object_or_404(Product, id=product.id)

                if prod.is_sale:
                    price = prod.seal_price
                else:
                    price = prod.price

                for key, value in quantities.items():
                    if int(key) == prod.id:
                        order_items = OrderItems(
                            user=shipping_user,
                            order=order_id,
                            product=prod,
                            quantity=value,
                            price=price,
                        )
                        order_items.save()
            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session[key]
            cu=Profile.objects.get(user__id=request.user.id)
            cu.old_cart=''
            cu.save()
            messages.success(request, 'سفارش شما با موفقیت ثبت شد')
            return redirect('home')
        else:
            new_order = Order(
                order_status=order_status,
                shipping_address_full_name=shipping_address_full_name,
                amount_paid=total_ordering,
            )
            new_order.save()

            order_id=get_object_or_404(Order,pk=new_order.pk)
            for product in products:
                prod=get_object_or_404(Product,id=product.id)

                if prod.is_sale:
                    price=prod.seal_price
                else:
                    price=prod.price

                for key, value in quantities.items():
                    if int(key)==prod.id:
                        order_items = OrderItems(
                            order=order_id,
                            product=prod,
                            quantity=value,
                            price=price,
                        )
                        order_items.save()
            for key in list(request.session.keys()):
                if key == 'session_key':
                    del request.session[key]
            messages.success(request, 'سفارش شما با موفقیت ثبت شد')
            return redirect('home')

        return render(request,'payment/order_process.html',{'shipping_info':shipping_info})
    else:
        messages.success(request, 'شما دسترسی به این صفحه را ندارید')
        return redirect('home')
