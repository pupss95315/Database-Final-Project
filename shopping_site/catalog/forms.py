from django import forms
from .models import Cart, Customer, Supplier, 


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["CID", "Password", "Firstname", "Lastname", "Gender", "BDate", "City"]


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["SName"]