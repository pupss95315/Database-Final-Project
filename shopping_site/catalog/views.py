from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime
from .models import Supplier, Customer, Product, Cart, Order, Warehouse
from .forms import SupplierForm, CustomerForm, ProductForm, OrderForm, WarehouseForm
from django.db.models import Q
from django.template import RequestContext
from .filters import SupplierFilter, CartFilter, OrderFilter, WarehouseFilter, ProductFilter

# add
def addSupplier(request): 
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
    if request.method == "POST":
        return HttpResponseRedirect("/addSuccessfully") 
    context = {'form': form}
    return render(request, 'createSupplier.html', context)


def addProduct(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    if request.method == "POST":
        return HttpResponseRedirect("/addSuccessfully") 
    context= {'form': form }
    return render(request, 'createProduct.html', context)
    
    

def addWarehouse(request):
    form = WarehouseForm(request.POST or None)
    if form.is_valid():
        form.save()
    if request.method == "POST":
        return HttpResponseRedirect("/addSuccessfully") 
    context= {'form': form }
    return render(request, 'createWarehouse.html', context)

def addCustomer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
    if request.method == "POST":
        return HttpResponseRedirect("/index") 
    context = {'form': form}
    return render(request, 'createCustomer.html', context)

# def deleteSupplier(request, id):
#     context ={} 
#     obj = get_object_or_404(Supplier, SID = id) 
#     if request.method == "POST": 
#         obj.delete() 
#         return HttpResponseRedirect("/deleteSuccessfully") 
#     return render(request, "delete.html", context) 



# search
def searchSupplier(request):
    supplier = Supplier.objects.all()
    supplierFilter = SupplierFilter(request.GET, queryset=supplier)
    return render(request, 'searchSupplier.html', {'filter': supplierFilter})

def searchProduct(request):
    product = Product.objects.all()
    productFilter = ProductFilter(request.GET, queryset=product)
    return render(request, 'searchProduct.html', {'filter': productFilter})

def searchWarehouse(request):
    warehouse = Warehouse.objects.all()
    warehouseFilter = WarehouseFilter(request.GET, queryset=warehouse)
    return render(request, 'searchWarehouse.html', {'filter': warehouseFilter})

def searchCart(request):
    cart = Cart.objects.all()
    cartFilter = CartFilter(request.GET, queryset=cart)
    return render(request, 'searchCart.html', {'filter': cartFilter})

def searchOrder(request):
    order = Order.objects.all()
    orderFilter = OrderFilter(request.GET, queryset=order) #queryset: query domain
    return render(request, 'searchOrder.html', {'filter': orderFilter})


#update
def updateSupplier(request, id):  
    context ={} 
    obj = get_object_or_404(Supplier, SID = id) 
    form = SupplierForm(request.POST or None, instance=obj)  
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id+"/showUpdatedSupplier") 
    context["form"] = form 
    return render(request, "update.html", context)

def updateProduct(request, id):  
    context ={} 
    obj = get_object_or_404(Product, PID = id) 
    form = ProductForm(request.POST or None, instance=obj)  
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id+"/showUpdatedProduct") 
    context["form"] = form 
    return render(request, "update.html", context)

def updateWarehouse(request, id):  
    context ={} 
    obj = get_object_or_404(Warehouse, WID = id) 
    form = WarehouseForm(request.POST or None, instance=obj)  
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id+"/showUpdatedWarehouse") 
    context["form"] = form 
    return render(request, "update.html", context)

def updateOrder(request, id):  
    context ={} 
    obj = get_object_or_404(Order, OrderID = id) 
    form = OrderForm(request.POST or None, instance=obj)  
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id+"/showUpdatedOrder") 
    context["form"] = form 
    return render(request, "update.html", context)

def updateCustomer(request, id):  
    context ={} 
    obj = get_object_or_404(Customer, CID = id) 
    form = CustomerForm(request.POST or None, instance=obj)  
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id+"/showUpdatedCustomer") 
    context["form"] = form 
    return render(request, "update.html", context)

# show
def showUpdatedSupplier(request, id): 
    context ={} 
    context["supplier"] = Supplier.objects.get(SID = id) 
    return render(request, "showUpdatedSupplier.html", context)

def showUpdatedProduct(request, id): 
    context ={} 
    context["product"] = Product.objects.get(PID = id) 
    return render(request, "showUpdatedProduct.html", context)

def showUpdatedWarehouse(request, id): 
    context ={} 
    context["warehouse"] = Warehouse.objects.get(WID = id) 
    return render(request, "showUpdatedWarehouse.html", context)
def showUpdatedCustomer(request, id): 
    context ={} 
    context["customer"] = Customer.objects.get(CID = id) 
    return render(request, "showUpdatedCustomer.html", context)
def showUpdatedOrder(request, id): 
    context ={} 
    context["order"] = Order.objects.get(OrderID = id) 
    return render(request, "showUpdatedOrder.html", context)


# delete
def deleteSupplier(request, id):
    context ={} 
    obj = get_object_or_404(Supplier, SID = id) 
    if request.method == "POST": 
        obj.delete() 
        return HttpResponseRedirect("/deleteSuccessfully") 
    return render(request, "delete.html", context) 

def deleteWarehouse(request, id):
    context ={} 
    obj = get_object_or_404(Warehouse, WID = id) 
    if request.method == "POST": 
        obj.delete() 
        return HttpResponseRedirect("/deleteSuccessfully") 
    return render(request, "delete.html", context) 

def deleteProduct(request, id):
    context ={} 
    obj = get_object_or_404(Product, PID = id) 
    if request.method == "POST": 
        obj.delete() 
        return HttpResponseRedirect("/deleteSuccessfully") 
    return render(request, "delete.html", context)

def deleteSuccessfully(request):
     return render(request, "deleteSuccessfully.html") 


#fail

def fail(request): 
    return render(request, "fail.html") 

def index(request): 
    return render(request, "index.html") 

def member_page(request): 
    return render(request, "member_page.html") 

def employee(request): 
    return render(request, "employee.html") 

def deleteInput_supplier(request): 
    return render(request, "deleteInput_supplier.html") 

def deleteInput_warehouse(request): 
    return render(request, "deleteInput_warehouse.html") 

def deleteInput_product(request): 
    return render(request, "deleteInput_product.html") 

def update_supplier(request): 
    return render(request, "update_supplier.html") 

def update_warehouse(request): 
    return render(request, "update_warehouse.html") 

def update_product(request): 
    return render(request, "update_product.html") 

def update_customer(request): 
    return render(request, "update_customer.html") 

def update_order(request): 
    return render(request, "update_order.html") 

def addSuccessfully(request): 
    return render(request, "addSuccessfully.html") 

# def updateSupplier(request, pk):  
#     supplier = get_object_or_404(SupplierForm, pk=pk)
#     if request.method == "POST":
#         form = SupplierForm(request.POST, instance=supplier)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})


# def searchSupplier(request):
#     supplier = get_object_or_404(SupplierForm, pk=pk)
#     search_post = request.GET.get("search")
#     form = SupplierForm(request.POST or None, instance=supplier)
#     if search_post:
#         posts = Supplier.objects.filter(Q(title_icontains=search_post) & Q(tcontent_icontains=search_post))
#     else:
#         posts = Supplier.objects.all()
#     context = {'form': form}
#     return render(request, 'updateSupplier.html', context)

# def searchSupplier(request):
#     suppliers = Supplier.objects.all()
#     form = SupplierForm()
#     #supplierFilter = SupplierFilter(queryset=supplier)

#     if request.method == "POST":
#         form = SupplierForm(request.POST)
#         if form.is_valid():
#             form.save()

#     context = {
#         'suppliers': suppliers,
#         'form': form
#     }
#     return render(request, 'searchSupplier.html', context)



# def showUpdatedSupplier(request, pk): 
#     context = {} 
#     context["data"] = SupplierForm.objects.get(id=pk) 
#     return render(request, "showUpdatedSupplier.html", context)


# def hello_world(request):
#     return render(request, 'hello_world.html', {
#         'current_time': str(datetime.now()),
#     })
# from catalog.models import Supplier, Customer

# def lookUpCart(request):
#     product_list = Cart.objects.filter(CartStatus = "in_cart")
#     return render(request, 'lookUpCart.html', {
#         'product_list': product_list,
#     })
# # def post_detail(request, pk):
# #     post = Post.objects.get(pk=int(pk))
# #     return render(request, 'post.html', {'post': post})

# def salesReport(request):

# def lookUpCost(request):
