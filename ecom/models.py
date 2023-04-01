from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name


class ProductCategory(models.Model):
    gender = models.CharField(max_length=40)
    clothing = models.CharField(max_length=100)
    shoes = models.CharField(max_length=40)
    accessories = models.CharField(max_length=50)
    bags = models.CharField(max_length=40)

    def __str__(self):
        return self.gender


class Product(models.Model):
    SIZES = (
        ('Size S', 'Size S'),
        ('Size M', 'Size M'),
        ('Size L', 'Size L'),
        ('Size XL', 'Size Xl'),
    )
    COLORS = (
        ('Black', 'Black'),
        ('White', 'White'),
        ('Blue', 'Blue'),
        ('Gray', 'Gray'),
    )
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50, null=True, choices=COLORS)
    size = models.CharField(max_length=50, null=True, choices=SIZES)
    item_count = models.PositiveIntegerField()
    banner_image = models.ImageField(upload_to='product_image/')
    image2 = models.ImageField(upload_to='product_image/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product_image/', null=True, blank=True)
    image4 = models.ImageField(upload_to='product_image/', null=True, blank=True)
    image5 = models.ImageField(upload_to='product_image/', null=True, blank=True)

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Order Confirmed', 'Order Confirmed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey('Customer', models.CASCADE, null=True)
    product = models.ForeignKey('Product', models.CASCADE, null=True)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    mobile = models.CharField(max_length=20)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS)



