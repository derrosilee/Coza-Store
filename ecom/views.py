from django.shortcuts import render, redirect, reverse
# from .models import Product, ProductCategory, Orders, Customer
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from . import models


# Create your views here.

def home(request):
    # products = models.Product.objects.all()
    # if 'product_ids' in request.COOKIES:
    #     products_ids = request.COOKIES['product_ids']
    #     counter = products_ids.split('|')
    #     product_count_in_cart = len(set(counter))
    # else:
    #     product_count_in_cart = 0
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect()
    return render(request, template_name='BaseTemplates/index.html')


def register(request):
    return render(request, template_name='BaseTemplates/users/register.html')


def login(request):
    return render(request, template_name='BaseTemplates/users/login.html')


def products_view(request):
    return render(request, template_name='BaseTemplates/product.html')


def product_detail(request):
    return render(request, template_name='BaseTemplates/product-detail.html')


def track_order(request):
    return render(request, template_name='BaseTemplates/track-order.html')


def cart(request):
    return render(request, template_name='BaseTemplates/shopping-cart.html')


def checkout(request):
    return render(request, template_name='BaseTemplates/checkout/checkout.html')


def about(request):
    return render(request, template_name='BaseTemplates/about.html')


def contact(request):
    return render(request, template_name='BaseTemplates/contact.html')


def admin_dashboard_view(request):
    return render(request, template_name='AdminTemplates/index.html')
