from django.shortcuts import render, redirect, HttpResponse
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def purchase(request):
    product = Product.objects.get(id = request.POST["id"])
    quantity_from_form = int(request.POST["quantity"])
    
    price_from_form = float(product.price) #price from data base
    total_charge = quantity_from_form * price_from_form
    if 'all' not in request.session:
        request.session['all'] = 0
    if 'order_all' not in request.session:
        request.session['order_all'] = 0    

    request.session['order_t'] = total_charge
    request.session['order_q'] =  quantity_from_form
    request.session['order_all'] +=  quantity_from_form
    request.session['all'] += total_charge
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    
    return redirect("/checkout")

def checkout(request):
    return render(request, "store/checkout.html")