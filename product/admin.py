from django.contrib import admin
from .models import (
    Vendor , 
    Product , 
    ProductVersion  , 
    Color , 
    Storage ,
    ProductImage , 
    VendorImage , 
    Platform , 
    ProductCategory , 
    Review,
    SubCategory,
    Wishlist
    )
from modeltranslation.admin import TranslationAdmin


class ProductImageInLine(admin.TabularInline):
    model = ProductImage

class VendorImageInLine(admin.TabularInline):
    model = VendorImage


@admin.register(ProductVersion)
class ProductAdmin(TranslationAdmin):
    list_display = ['product_id' , 'color_id' , 'storage_id']
    inlines = [ProductImageInLine]


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    inlines = [VendorImageInLine]



admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Storage)
admin.site.register(VendorImage)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)
admin.site.register(Platform)
admin.site.register(Review)
admin.site.register(SubCategory)
admin.site.register(Wishlist)

