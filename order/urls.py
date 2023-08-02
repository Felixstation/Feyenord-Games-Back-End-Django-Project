from django.urls import path
from order.views import *


app_name = 'order'

urlpatterns = [
    path('update_item/' , UpdateItem , name = 'update_item'),
    path('cart/' , cart , name = 'cart'),
    path('checkout/' , checkout , name = 'checkout'),
    path('process_order/' , processOrder , name='process_order'),
    path('order-success' , orderSuccess , name= 'order-success')

]