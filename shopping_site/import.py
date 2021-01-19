import csv,sys,os
project_dir = "/shopping_site/"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'shopping_site.settings'
import django
django.setup()


from catalog.models import Product
from catalog.models import Customer
from catalog.models import Cart
from catalog.models import Order
from catalog.models import Warehouse
from catalog.models import Supplier
from catalog.models import Store
from catalog.models import Supply

# from DBapp.models import ProductAdmin
# from DBapp.models import CustomerAdmin
# from DBapp.models import CartAdmin
# from DBapp.models import OrderAdmin
# from DBapp.models import WarehouseAdmin
# from DBapp.models import SupplierAdmin


# delete
entries = Product.objects.all()
entries.delete()
entries = Customer.objects.all()
entries.delete()
entries = Cart.objects.all()
entries.delete()
entries = Order.objects.all()
entries.delete()
entries = Warehouse.objects.all()
entries.delete()
entries = Supplier.objects.all()
entries.delete()
entries = Store.objects.all()
entries.delete()
entries = Supply.objects.all()
entries.delete()


productData = csv.reader(open("./ProductData.csv"),delimiter=",")
for row in productData:
	if row[0] != 'PID':
		unit = Product()
		unit.PID = row[0]
		unit.PName = row[1]
		unit.product_size = row[2]
		unit.price = row[3]
		unit.category = row[4]
		unit.save()

customerData = csv.reader(open("./CustomerData.csv"),delimiter=",")
for row in customerData:
	if row[0] != 'CID':
		unit = Customer()
		unit.CID = row[0]
		unit.Password = row[1]
		unit.Firstname = row[2]
		unit.Lastname = row[3]
		unit.Gender = row[4]
		unit.BDate = row[5]
		unit.City = row[6]
		unit.save()

cartData = csv.reader(open("./CartData.csv"),delimiter=",")
for row in cartData:
	if row[0] != 'CartID':
		unit = Cart()
		unit.CartID = row[0]
		cus = Customer.objects.get(CID=row[1])
		unit.customer = cus
		pro = Product.objects.get(PID=row[2])
		unit.product = pro
		unit.cart_status = row[3]
		unit.save()

orderData = csv.reader(open("./OrderData.csv"),delimiter=",")
for row in orderData:
	if row[0] != 'orderID':
		unit = Order()
		unit.OrderID = row[0]
		car = Cart.objects.get(CartID=row[1])
		unit.cart = car
		unit.quantity = row[2]
		unit.order_status = row[3]
		unit.order_date = row[4]
		unit.transaction_price = row[5]
		unit.save()

warehouseData = csv.reader(open("./WarehouseData.csv"),delimiter=",")
for row in warehouseData:
	if row[0] != 'WID':
		unit = Warehouse()
		unit.WID = row[0]
		unit.location = row[1]
		unit.save()

supplierData = csv.reader(open("./SupplierData.csv"),delimiter=",")
for row in supplierData:
	if row[0] != 'SID':
		unit = Supplier()
		unit.SID = row[0]
		unit.SName = row[1]
		unit.save()

storeData = csv.reader(open("./StoreData.csv"),delimiter=",")
for row in storeData:
	if row[0] != 'PID':
		unit = Store()
		pro = Product.objects.get(PID=row[0])
		unit.PID = pro
		war = Warehouse.objects.get(WID=row[1])
		unit.WID = war
		unit.Quantity = row[2]
		unit.save()

supplyData = csv.reader(open("./SupplyData.csv"),delimiter=",")
for row in supplyData:
	if row[0] != 'PID':
		unit = Supply()
		pro = Product.objects.get(PID=row[0])
		unit.PID = pro
		sup = Supplier.objects.get(SID=row[1])
		unit.SID = sup
		unit.UnitCost = row[2]
		unit.save()