from product.models import Platform

def platform(request):
    platform = Platform.objects.all()

    return {
        'platform': platform
    }




from product.models import Platform
from order.models import Order
def cont_proc(request):
    platform = Platform.objects.all()
    
        
    if request.user.is_authenticated:
            user = request.user
            order , created = Order.objects.get_or_create(user = user , complete = False)
            items = order.orderitem_set.all()
            cardItems = order.get_cart_items
            
    else: 
            items = []
            order = {'get_cart_total': 0 , 'get_cart_items' : 0  , 'shipping': False}
            cardItems = order['get_cart_items']
    context = {'items' : items,
                   'order' : order,
                   'cont_proc':platform
               }
    return context