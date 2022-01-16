from django.urls import path
from lab4 import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ice-creams', views.ice_cream_data, name='ice_cream_index'),
    path('ice-creams/<int:code>', views.ice_cream_show, name='ice_cream_show'),
    path('shops', views.shop_data, name='shop_index'),
]
