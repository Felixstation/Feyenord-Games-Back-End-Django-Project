from rest_framework import serializers
from product.models import Product , Vendor , ProductCategory , ProductVersion, Review
from core.models import Subscriber
from account.models import User
from django_filters.rest_framework import DjangoFilterBackend

class UserSerializer(serializers.ModelSerializer):
    imageURL = User.imageURL
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'image',
            'imageURL'
            
        )


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            'id',
            'name',
            'about'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory

        fields = (
            'id',
            'name',

        )


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory

        fields = (
            'id',
            'name',

        )



class ProductSerializer(serializers.ModelSerializer):
    # vendor_id = serializers.CharField(source = 'vendor_id.name')
    vendor_id = VendorSerializer()
    category_id = CategorySerializer()

    class Meta:
        model = Product
        fields = ( 
            'id',
            'name',
            'vendor_id',
            'category_id'


        )


class ProductCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = ( 
            'id',
            'name',
            'vendor_id',
            'category_id'


        )


class ProductVersionSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()
    thumbnail = ProductVersion.imageURL
    
    class Meta:
        model = ProductVersion

        fields = (
            'id',
            'product_id',
            'price',
            'description',
            'slug',
            'color_id',
            'storage_id',
            'platform_id',
            'thumbnail',
            'get_absolute_url'


        )


class ProductVersionCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only = True)

    class Meta:
        model = ProductVersion
         
        fields = (
            'id',
            'product_id',
            'price',
            'description',
            'slug',
            'color_id',
            'storage_id',
            'platform_id',
            'thumbnail'


        )


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber

        fields = (
            'email',
        )


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Review


        fields = (
            'user',
            'product_version',
            'content',
            'created_at'
        )


class ProductIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVersion

        fields = (
            'id',
        )


class CreateReviewSerializer(serializers.ModelSerializer):
    product_version = ProductVersionSerializer
    class Meta:
        model = Review
        fields = ('user', 'product_version', 'content')