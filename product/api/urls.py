from django.urls import path
from product.api.views import (
    vendors , 
    ProductCreateAPIView,
    ProductVersionCreateAPIView,
    ProductVersionRetrieveUpdateDestroyAPIView,
    CatRetrieveUpdateDestroyAPIView,
    CatCreateAPIView,
    SubscriberCreateAPIView,
    ProductReviewRetrieveAPIView,
    ReviewCreateAPIView
        )

urlpatterns = [
    path('products/' , ProductVersionCreateAPIView.as_view() , name = 'products'),
    path('vendors/', vendors , name = 'vendors'),
    path('categories/' , CatCreateAPIView.as_view() , name = 'categories'),
    path('categories/<int:id>' , CatRetrieveUpdateDestroyAPIView.as_view() , name = 'categories'),
    path('products/<int:pk>' , ProductVersionRetrieveUpdateDestroyAPIView.as_view() , name = 'product_versions'),
    path('subscribers/' , SubscriberCreateAPIView.as_view() , name = 'subscribers') ,
    path('products/<int:product_id>/comments/', ProductReviewRetrieveAPIView.as_view(), name='product-comment-retrieve'),
    path('products/<int:product_id>/comments/create/', ReviewCreateAPIView.as_view(), name='product-create'),

]