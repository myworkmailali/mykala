
from django.urls import path,include
#from .views import index, about, login_user,logout_user
from . import views


urlpatterns = [

    path('', views.index,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('signup/',views.signup_user,name='signup'),
    path('profile/',views.update_profile,name='profile'),
    path('update_password/',views.update_password,name='update_password'),
    path('user_info/',views.user_info,name='user_info'),
    path('search/',views.search,name='search'),
    path('search_quic/', views.search_quic, name='search_quic'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:cat>',views.category,name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('orders/', views.user_orders, name='user_orders'),
    path('orders_details/<int:pk>', views.orders_details, name='orders_details'),

]
