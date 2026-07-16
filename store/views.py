from django.shortcuts import render,get_object_or_404, redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'web/index.html',{'products': products})
    
def product_detail(request,pk):
    products = get_object_or_404(Product, pk=pk)
    return render(request,'web/product_detail.html',{'products':products})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'web/signup.html', {'form': form})


