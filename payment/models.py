from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.db.models.signals import post_save

class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shipping_address_full_name=models.CharField(max_length=100)
    shipping_address_email=models.CharField(max_length=100)
    shipping_address_address = models.CharField(max_length=100, blank=True)
    shipping_address_city = models.CharField(max_length=100, blank=True)
    shipping_address_state = models.CharField(max_length=100, blank=True)
    shipping_address_zipcode = models.CharField(max_length=100, blank=True)
    shipping_address_phone = models.CharField(max_length=100, blank=True)
    shipping_address_country = models.CharField(max_length=100, default='Iran')
    shipping_address_old_cart = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return f'Shipping addresses form {self.user.username}'

    class Meta:
        verbose_name = 'Shipping Address'
        verbose_name_plural = 'Shipping Addresses'
def create_shipping(sender,instance,created,**kwargs):
   if created:
       user_shipping=ShippingAddress(user=instance)
       user_shipping.save()

post_save.connect(create_shipping, sender=User)

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
            ('pending','آماده پرداخت'),
            ('processing','درحال پردازش سفارش'),
            ('shipping','ارسال به مشتری'),
            ('delivered','تحویل به مشتری'),
            ]
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=250)
    email=models.EmailField(max_length=250,blank=True)
    shipping_address_full_name=models.CharField(max_length=15000)
    amount_paid=models.DecimalField(decimal_places=0,max_digits=10)
    date_ordered=models.DateField(auto_now_add=True)
    order_status=models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES,default='pending')
    def __str__(self):
        return f'Order form {self.id}'


class OrderItems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(decimal_places=0,max_digits=10)
    def __str__(self):
        return f'Order items form {self.id}'
