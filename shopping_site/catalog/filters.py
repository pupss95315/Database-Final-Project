from .models import Supplier, Cart, Order, Warehouse, Product
import django_filters


class SupplierFilter(django_filters.FilterSet):

    class Meta:
        model = Supplier
        fields = ["SName"]

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ["PID", "PName", "product_size", "price", "category"]

class CartFilter(django_filters.FilterSet):
    class Meta:
        model = Cart
        fields = ["customer"]


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ('cart', 'OrderID', 'order_status', 'order_date', 'quantity', 'transaction_price')


class WarehouseFilter(django_filters.FilterSet):
    class Meta:
        model = Warehouse
        fields = ('WID', 'location')