from django.contrib import admin
from .models import Cart
from .models import Product
from .models import Order
from .models import Warehouse
from .models import Customer
from .models import Supplier
from .models import Store
from .models import Supply

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('SName')


admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Warehouse)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Store)
admin.site.register(Supply)
