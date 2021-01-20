from django import forms
from .models import Customer, Supplier, Product, Cart, Order, Warehouse


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["CID", "Password", "Firstname", "Lastname", "Gender", "BDate", "City"]


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["SName", "SID"]

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= ['PID', 'PName', 'product_size', 'price', 'category']

class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields=['OrderID', 'order_status', 'order_date', 'cart', 'quantity', 'transaction_price']
    
class WarehouseForm(forms.ModelForm):
    class Meta:
        model= Warehouse
        fields=['WID', 'location']
