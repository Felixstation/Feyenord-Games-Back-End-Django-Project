from django.forms.models import BaseModelForm
from django.http import HttpResponse , JsonResponse
from django.shortcuts import render , redirect
from .forms import CheckoutForm
from django.views.generic import CreateView
from .models import Checkout , Order , OrderItem
from product.models import ProductVersion , ProductImage
from django.urls import reverse_lazy
import json
# from .utils import cookieCart, cartData, guestOrder
import datetime
from django.contrib import messages



def checkout(request):
    # form = CheckoutForm()
    if request.user.is_authenticated:
        # if request.method == 'POST':
        #     form = CheckoutForm(data = request.POST)
        #     if form.is_valid():
        #         form.save()
        user = request.user
        order , created = Order.objects.get_or_create(user = user , complete = False)
        items = order.orderitem_set.all()

    else: 
        items = []
        order = {'get_cart_total': 0 , 'get_cart_items' : 0 , 'shipping' : False}

    
    context = {
        'items' : items,
        'order' : order
    }

    return render(request , 'checkout.html' , context)


def cart(request):

    if request.user.is_authenticated:
        user = request.user
        order , created = Order.objects.get_or_create(user = user , complete = False)
        items = order.orderitem_set.all()

    else: 
        items = []
        order = {'get_cart_total': 0 , 'get_cart_items' : 0 }

    context = {'items' : items,
               'order' : order
               }

    return render(request , 'cart.html' , context)



def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action:' , action)
    print('productId:' , productId)


    customer = request.user
    product = ProductVersion.objects.get(id = productId)
    order, created = Order.objects.get_or_create(user=customer, complete=False)
    orderItem , created = OrderItem.objects.get_or_create(order = order , product = product)
    if action == 'add':
        messages.success(request, "Item Succesfully Added!") 
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        messages.success(request, "Item Succesfully Removed!") 
    elif action == 'delete':
        messages.success(request, "Item Succesfully Deleted!") 
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
    
    
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    user = request.user
    data = json.loads(request.body)
    order , created = Order.objects.get_or_create(user = user , complete = False)
    total = float(data['form']['total'])
    order.transaction_id= transaction_id

    if total == order.get_cart_total:
        order.complete = True
        

    order.save()

    if order.shipping == True:
        Checkout.objects.create(
            user = user,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['county'],
            zipcode= data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete!' , safe=False)


def orderSuccess(request):
    user = request.user
    order = Order.objects.filter(user = user).reverse().first()

    context = {
        'order': order
    }

    return render(request , 'order-success.html' , context)