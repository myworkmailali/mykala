from django.urls import path,include
from . import views


urlpatterns = [

    path('payment_success/', views.payment_success,name='payment_success'),
    path('checkout/', views.checkout,name='checkout'),
    path('order_confirm/', views.order_confirm,name='order_confirm'),
]
