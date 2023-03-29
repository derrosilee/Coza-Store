from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, template_name='BaseTemplates/index.html')


def products(request):
    return render(request, template_name='BaseTemplates/product.html')


def product_detail(request):
    return  render(request, template_name='BaseTemplates/product-detail.html')
