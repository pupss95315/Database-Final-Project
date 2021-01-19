"""shopping_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
""" 
from django.conf.urls import include, url
from django.contrib import admin
from catalog.views import addSupplier, addProduct, addWarehouse, addCustomer
from catalog.views import searchSupplier, searchProduct, searchWarehouse, searchCart, searchOrder
from catalog.views import updateSupplier, updateProduct, updateWarehouse, updateCustomer, updateOrder
from catalog.views import showUpdatedSupplier, showUpdatedProduct, showUpdatedWarehouse, showUpdatedCustomer, showUpdatedOrder 
from catalog.views import deleteSupplier, deleteProduct, deleteWarehouse,  deleteSuccessfully, fail
from django.urls import path 
# from catalog.views import hello_world
# from catalog.views import 

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^addSupplier/$', addSupplier),
    url(r'^addProduct/$', addProduct),
    url(r'^addWarehouse/$', addWarehouse),
    url(r'^addCustomer/$', addCustomer),

    url(r'^searchSupplier/$', searchSupplier),
    url(r'^searchProduct/$', searchProduct),
    url(r'^searchWarehouse/$', searchWarehouse),
    url(r'^searchCart/$', searchCart),
    url(r'^searchOrder/$', searchOrder),

    path('<id>/updateSupplier', updateSupplier),
    path('<id>/updateProduct', updateProduct), 
    path('<id>/updateWarehouse', updateWarehouse), 
    path('<id>/updateCustomer', updateCustomer),
    path('<id>/updateOrder', updateOrder),

    path('<id>/deleteSupplier', deleteSupplier),
    path('<id>/deleteProduct', deleteProduct),
    path('<id>/deleteWarehouse', deleteWarehouse),
    path('deleteSuccessfully', deleteSuccessfully),

    path('<id>/showUpdatedSupplier', showUpdatedSupplier), 
    path('<id>/showUpdatedProduct', showUpdatedProduct), 
    path('<id>/showUpdatedWarehouse', showUpdatedWarehouse),
    path('<id>/showUpdatedCustomer', showUpdatedCustomer), 
    path('<id>/showUpdatedOrder', showUpdatedOrder), 

    url(r'^fail/$', fail),

    #path('showCreatedCustomer', showCreatedCustomer),
    #url(r'^showSearch/$', searchSupplier),
    #url(r'^showUpdatedSupplier/(?P<pk>\d+)/$', showUpdatedSupplier), 
    #url(r'^updateSupplier/(?P<pk>\d+)/$', updateSupplier), 
    #url(r'^hello/$', hello_world),
    #url(r'^$', home),
    #url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),
]
