from django.urls import path
from .views import home, checkout, products

app_name = 'core'

urlpatterns = [
    path('', home, name='item-list'),
    path('checkout/', checkout, name='checkout'),
    path('products/', products, name='products'),
]
