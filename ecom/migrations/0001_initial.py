# Generated by Django 4.1.7 on 2023-03-31 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(null=True, upload_to='profile_pic/CustomerProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=40)),
                ('clothing', models.CharField(max_length=100)),
                ('shoes', models.CharField(max_length=40)),
                ('accessories', models.CharField(max_length=50)),
                ('bags', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Blue', 'Blue'), ('Gray', 'Gray')], max_length=50, null=True)),
                ('size', models.CharField(choices=[('Size S', 'Size S'), ('Size M', 'Size M'), ('Size L', 'Size L'), ('Size XL', 'Size Xl')], max_length=50, null=True)),
                ('item_count', models.PositiveIntegerField()),
                ('banner_image', models.ImageField(upload_to='product_image/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('mobile', models.CharField(max_length=20)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Order Confirmed', 'Order Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=50)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.product')),
            ],
        ),
    ]
