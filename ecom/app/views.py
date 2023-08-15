from django.shortcuts import render,redirect
from .models import Product
# Create your views here.



def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})

def product_detail(request,id):
    this_product = Product.objects.get(stock=id)
    return render(request,'product.html',{'this_product': this_product})


