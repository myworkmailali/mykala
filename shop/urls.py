
from django.urls import path,include
#from .views import index, about, login_user,logout_user
from . import views


urlpatterns = [

    path('', views.index,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('signup/',views.signup_user,name='signup'),
]
