from django.db import models
from django.contrib.auth.models import User

class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, default='Iran')
    old_cart = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return f'Shipping addresses form {self.user.username}'

    class Meta:
        verbose_name = 'Shipping Address'
        verbose_name_plural = 'Shipping Addresses'