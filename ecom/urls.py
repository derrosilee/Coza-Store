from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('products_view/', views.products_view, name='products_view'),
    path('search', views.search_view, name='search'),
    path('add-to-cart/<int:pk>/', views.add_to_cart_view, name='add-to-cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view, name='remove-from-cart'),
    path('customer-home', views.customer_home_view, name='customer-home'),
    path('payment-success', views.payment_success_view, name='payment-success'),
    path('customer-address', views.customer_address_view, name='customer-address'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('track_order/', views.track_order, name='track_order'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('admin_dashboard_view/', views.admin_dashboard_view, name='admin_dashboard_view'),
    path('admin-add-product', views.admin_add_product_view, name='admin-add-product'),
    path('admin-view-booking', views.admin_view_booking_view, name='admin-view-booking'),
    path('update-product/<int:pk>', views.update_product_view, name='update-product'),
    path('admin-products', views.admin_products_view, name='admin-products'),
    path('delete-product/<int:pk>', views.delete_product_view, name='delete-product'),

    path('view-customer', views.view_customer_view, name='view-customer'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
