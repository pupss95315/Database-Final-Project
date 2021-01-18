from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
#from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
#from datetime import datetime
from .models import Supplier, Customer
from .forms import SupplierForm, CustomerForm
from django.db.models import Q
from django.template import RequestContext
from .filters import SupplierFilter


def addCustomer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'createCustomer.html', context)


def addSupplier(request): 
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'createSupplier.html', context)


def updateSupplier(request, id):  
    context ={} 
    obj = get_object_or_404(Supplier, SID = id) 
    form = SupplierForm(request.POST or None, instance=obj)  
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id) 
    context["form"] = form 
    return render(request, "updateSupplier.html", context)

def showUpdatedSupplier(request, id): 
    context ={} 
    context["supplier"] = Supplier.objects.get(SID = id) 
    return render(request, "showUpdatedSupplier.html", context)

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

def searchSupplier(request):
    supplier = Supplier.objects.all()
    supplierFilter = SupplierFilter(request.GET, queryset=supplier)
    return render(request, 'searchSupplier.html', {'filter': supplierFilter})

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


def hello_world(request):
    return HttpResponse("Hello World!")