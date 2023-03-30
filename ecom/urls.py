from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('products/', views.products, name='products'),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('track_order/', views.track_order, name='track_order'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
