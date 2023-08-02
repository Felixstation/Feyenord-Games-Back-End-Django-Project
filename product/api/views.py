from product.models import Product , Vendor , ProductCategory , ProductVersion , Review
from core.models import Subscriber
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from product.api.serializers import (
    ProductSerializer , 
    VendorSerializer , 
    CategorySerializer , 
    ProductCreateSerializer,
    CategoryCreateSerializer,
    ProductVersionSerializer,
    ProductVersionCreateSerializer,
    SubscriberSerializer,
    ReviewSerializer,
    CreateReviewSerializer
    )
from rest_framework.decorators import api_view
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView , 
    ListCreateAPIView , 
    CreateAPIView,
    RetrieveAPIView
    )
from rest_framework import filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from product.api.filters import ProductVersionFilter

def vendors(request):
    vendor_list = Vendor.objects.all()
    serializer = VendorSerializer(vendor_list , many = True)
    return JsonResponse(data= serializer.data , safe = False )


class CatRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryCreateSerializer
    queryset = ProductCategory.objects.all()


class CatCreateAPIView(ListCreateAPIView):
    serializer_class = CategoryCreateSerializer
    queryset = ProductCategory.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategorySerializer
        return self.serializer_class


class ProductCreateAPIView(ListCreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return self.serializer_class


class ProductVersionCreateAPIView(ListCreateAPIView):
    serializer_class = ProductVersionCreateSerializer
    queryset = ProductVersion.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = ['product_id__name' , 'description' , 'price' , 'color_id__name' , 'storage_id__name' , 'platform_id__name']
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ProductVersionFilter
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductVersionSerializer
        return self.serializer_class
    

class ProductVersionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductVersionCreateSerializer
    queryset = ProductVersion.objects.all()

    
class SubscriberCreateAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()


class ProductReviewRetrieveAPIView(APIView):
    def get(self, request, product_id):
        try:
            product = ProductVersion.objects.get(pk=product_id)
            review = Review.objects.filter(product_version=product)
        except ProductVersion.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class ReviewCreateAPIView(CreateAPIView):
    serializer_class = CreateReviewSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs['product_id']
        print(product_id)
        product = ProductVersion.objects.get(pk=product_id)
        serializer.save(product_version=product)



# @api_view(http_method_names=['GET' , 'POST'])
# def categories(request):
#     if request.method == 'POST':
#         serializer = CategoryCreateSerializer(data = request.data , context = {'request' : request})
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data = serializer.data , safe= False , status = 201) 
#         return JsonResponse(data = serializer.errors , safe= False , status = 400)
#     cat_list = ProductCategory.objects.all()
#     serializer = CategorySerializer(cat_list , context = {'request' : request},  many = True)
#     return JsonResponse(data = serializer.data , safe= False)


# @api_view(http_method_names=['PUT' , 'PATCH'])
# def cat_read_update(request , id):
#     if request.method == 'PUT':
#         category = ProductCategory.objects.get(id = id)
#         serializer = CategoryCreateSerializer(data = request.data ,context = {'request' : request} , instance= category)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data = serializer.data , safe= False , status = 201) 
#         return JsonResponse(data = serializer.errors , safe= False , status = 400)
    
#     if request.method == 'PATCH':
#         category = ProductCategory.objects.get(id = id)
#         serializer = CategoryCreateSerializer(data = request.data ,partial = True ,context = {'request' : request} , instance= category)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data = serializer.data , safe= False , status = 201) 
#         return JsonResponse(data = serializer.errors , safe= False , status = 400)


# @api_view(http_method_names= ['GET' , 'POST'])
# def products(request):
#     if request.method == 'POST':
#         serializer = ProductCreateSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data= serializer.data , safe=False , status = 201)
#         return JsonResponse(data= serializer.errors , safe=False , status = 400)
#     product_list = Product.objects.all()
#     # product_dict_list = []

#     # for product in product_list:
#     #     product_dict_list.append(
#     #         {'product_id' : product.id,
#     #          'product_name' : product.name,
#     #     })
#     serializer = ProductSerializer(product_list, context = {'request' : request} ,many = True)
#     return JsonResponse(data= serializer.data , safe=False)



# @api_view(http_method_names= ['GET' , 'POST'])
# def product_versions(request):
#     if request.method == 'POST':
#         serializer = ProductVersionCreateSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data = serializer.data , safe = False , status = 201)
#         return JsonResponse(data = serializer.errors , safe = False , status = 400)
    
#     product_version_list = ProductVersion.objects.all()
#     serializer = ProductVersionSerializer(product_version_list ,  context = {'request' : request} , many = True)

#     return JsonResponse(data = serializer.data , safe= False)

