
from django.urls import path,include
from .views import index, about, login_user,logout_user

urlpatterns = [

    path('', index,name='home'),
    path('about/',about,name='about'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout')
]
