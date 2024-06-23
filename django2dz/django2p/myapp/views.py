from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm

# Create new client
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('client_list'))
    else:
        form = ClientForm()
    return render(request, 'myapp/client_form.html', {'form': form})

# List clients
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'myapp/client_list.html', {'clients': clients})

# Create new product
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product_list'))
    else:
        form = ProductForm()
    return render(request, 'myapp/product_form.html', {'form': form})

# List products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

# Create new order
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_amount = sum(item.price for item in order.products.all())
            order.save()
            form.save_m2m()  # To save the many-to-many relationship
            return HttpResponseRedirect(reverse('order_list'))
    else:
        form = OrderForm()
    return render(request, 'myapp/order_form.html', {'form': form})

# List orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'myapp/order_list.html', {'orders': orders})