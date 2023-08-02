from django_filters.rest_framework import FilterSet
from product.models import ProductVersion


class ProductVersionFilter(FilterSet):
    class Meta:
        model = ProductVersion

        fields = {
            'product_id__category_id': ['exact'],
            'price' : ['gt' , 'lt'],
            'color_id' : ['exact'],
            'storage_id': ['exact']
        }

