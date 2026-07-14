from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'web/index.html',{'products': products})
    
def product_detail(request,pk):
    products = get_object_or_404(Product, pk=pk)
    return render(request,'web/product_detail.html',{'products':products})