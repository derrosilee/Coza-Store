from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, template_name='BaseTemplates/index.html')


def products(request):
    return render(request, template_name='BaseTemplates/product.html')


def product_detail(request):
    return render(request, template_name='BaseTemplates/product-detail.html')


def track_order(request):
    return render(request, template_name='BaseTemplates/track-order.html')


def cart(request):
    return render(request, template_name='BaseTemplates/shopping-cart.html')


def about(request):
    return render(request, template_name='BaseTemplates/about.html')


def contact(request):
    return render(request, template_name='BaseTemplates/contact.html')
