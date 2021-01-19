from django.db import models
from django.contrib import admin

# Create your models here.

class Product(models.Model):
    PRODUCT_SIZES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )
    PID = models.CharField(primary_key=True, max_length=10)
    PName = models.CharField(max_length=50)
    product_size = models.CharField(max_length=50, choices=PRODUCT_SIZES)
    price = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.PID

# class ProductAdmin(admin.ModelAdmin):
# 	list_display = ('PID', 'PName')


class Customer(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    CID = models.CharField(primary_key=True, max_length=10)
    Password = models.CharField(max_length=50)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10, choices = GENDER)
    BDate = models.DateField()
    City = models.CharField(max_length=50)
    def __str__(self):
        return str(self.CID)

# class CustomerAdmin(admin.ModelAdmin):
# 	list_display = ('CID', 'Firstname')

class Cart(models.Model):
    CART_STATUS = (
        ('D', 'deleted'),
        ('O', 'ordered'),
        ('C', 'in_cart'),
    )
    CartID = models.CharField(primary_key=True, max_length=10)
    cart_status = models.CharField(max_length=50, default='NULL', choices = CART_STATUS)
    customer = models.ForeignKey(Customer, related_name = "carts", on_delete=models.CASCADE, unique=False)
    product = models.ForeignKey(Product, related_name = "carts", on_delete=models.CASCADE, unique=False)
    
    # class Meta:
    #     together = ('customer', 'product')
    def __str__(self):
        return str(self.CartID)

# class CartAdmin(admin.ModelAdmin):
# 	list_display = ('CartID', 'cart_status')



class Order(models.Model):
    ORDER_STATUS = (
        ('O', 'ordered'),
        ('S', 'in shipping'),
        ('F', 'finished'),
    )
    OrderID = models.CharField(primary_key=True, max_length=10)
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS)
    order_date = models.DateField()
    cart = models.ForeignKey(Cart, related_name ='orders', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_price = models.IntegerField()

    class Meta:
        unique_together = ('cart' , 'OrderID')

    def __str__(self):
        return str(self.OrderID)

# class OrderAdmin(admin.ModelAdmin):
# 	list_display = ('OrderID', 'order_status')

class Warehouse(models.Model):
    WID = models.CharField(primary_key=True, max_length=10)
    location = models.CharField(max_length=100)

    def __str__(self):
        return str(self.WID)

# class WarehouseAdmin(admin.ModelAdmin):
# 	list_display = ('WID', 'location')



class Supplier(models.Model):
    SID = models.CharField(primary_key=True, max_length=10)
    SName = models.CharField(max_length=50)
    class Meta:
        unique_together = ('SID', 'SName')
    def __str__(self):
        return str(self.SID)

# class SupplierAdmin(admin.ModelAdmin):
# 	list_display = ('SID', 'SName')

class Store(models.Model):
    Quantity = models.IntegerField(default=0)
    PID = models.ForeignKey(Product, on_delete=models.CASCADE)
    WID = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('PID', 'WID')
    # def __str__(self):
    #     return self.Meta


class Supply(models.Model):
    UnitCost = models.IntegerField()
    PID = models.ForeignKey(Product, on_delete=models.CASCADE)
    SID = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('PID', 'SID')
    # def __str__(self):
    #     return self.Meta
