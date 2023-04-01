from django.contrib import admin
from .models import Customer, Product, Orders, ProductCategory


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


# class ProductCategoryAdmin(admin.ModelAdmin):
#     pass


admin.site.register(ProductCategory)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Orders, OrderAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.
