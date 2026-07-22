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


def add_to_cart(request,pk):
    product = get_object_or_404(Product,pk=pk)
    quantity = int(request.POST.get('quantity',1))
    cart = request.session.get('cart',{})
    pk_str = str(pk)
    if pk_str in cart:
        cart[pk_str] += quantity
    else:
        cart[pk_str] = quantity
    request.session['cart'] = cart 
    return redirect('view_cart') 

def view_cart(request):
    cart = request.session.get('cart',{})      
    cart_items = []
    total = 0
    for pk_str,quantity in cart.items():
        product = get_object_or_404(Product, pk=pk_str)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'web/cart.html', {'cart_items': cart_items, 'total': total})   


def remove_from_cart(request,pk):
    cart = request.session.get('cart', {})
    pk_str = str(pk)
    if pk_str in cart:
        del cart[pk_str]
        request.session['cart'] = cart
    return redirect('view_cart')    



