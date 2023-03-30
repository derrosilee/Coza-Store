from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('track_order/', views.track_order, name='track_order')
]