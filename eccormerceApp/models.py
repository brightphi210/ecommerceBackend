from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name  

class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, max_length=255, null=True)
    price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    

class OrderItemModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.product.name

class OrderModel(models.Model):
    STATUS_CHOICES = [
        ('processing', 'processing'),
        ('intrasit', 'intrasit'),
        ('delivered', 'delivered'),
        ('declined', 'declined'),
    ]
    status = models.CharField(choices = STATUS_CHOICES, max_length=255, null=True, blank=True)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, null=True, blank=True)
    orderItems = models.ForeignKey(OrderItemModel, on_delete=models.CASCADE, null=True, blank=True)
    order_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.orderItems.product.name


