from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('all-products/' , AllProductView.as_view() , name ='all_products' ),
    path('productpage/<str:slug>/', ProductDetailView.as_view(), name='productpage'),
    path('export' , export_view , name='export' ),
    path('wishlist/', wishlist_view, name='wishlist_view'),
    path('add_to_wishlist/<str:slug>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<str:slug>/', remove_from_wishlist, name='remove_from_wishlist')
]