from django.urls import path
from . import views  

urlpatterns = [
    path('', views.products, name='products'),
    path('details/<int:proid>/', views.detail, name='detail'),
    path('cats/<int:proid>/', views.cats, name='cats'),
    path('cart/<int:proid>/', views.carts, name='carts'),
    path('cartitem/', views.cartitem, name='cartitem'),
    path('delet/<int:proid>/', views.delet, name='delet'),
    
]