from django.db import models
from django.contrib.auth.models import User

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