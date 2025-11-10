from django.contrib.auth.models import User
from django import forms
from .models import ShippingAddress
class ShippingAddressForm(forms.ModelForm):
    shipping_address_full_name = forms.CharField(label='',
                              max_length=100,
                              required=False,
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'نام تحویل گیرنده'
                              }))
    shipping_address_address = forms.CharField(label='',
                              max_length=100,
                              required=False,
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'آدرس  گیرنده'
                              }))
    shipping_address_city = forms.CharField(label='',
                           max_length=100,
                           required=False,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'شهر'
                           }))
    shipping_address_state = forms.CharField(label='',
                            max_length=100,
                            required=False,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'نام استان'
                            }))
    shipping_address_zipcode = forms.CharField(label='',
                              max_length=100,
                              required=False,
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'کد پستی'
                              }))
    shipping_address_phone = forms.CharField(label='',
                            max_length=100,
                            required=False,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'شماره تلفن'
                            }))
    shipping_address_country = forms.CharField(label='',
                              max_length=100,
                              required=False,
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'کشور'
                              }))

    class Meta:
        model = ShippingAddress
        fields = ('shipping_address_full_name', 'shipping_address_address','shipping_address_city','shipping_address_phone','shipping_address_state','shipping_address_country','shipping_address_zipcode',
                  'shipping_address_phone','shipping_address_country'
                  )