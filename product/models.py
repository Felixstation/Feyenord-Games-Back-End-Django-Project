from django.db import models
from account.models import User
from django.urls import reverse_lazy , reverse



class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.name
    

class VendorImage(models.Model):
    vendor_image = models.ImageField(upload_to='vendor_images')
    vendor = models.ForeignKey('product.Vendor', on_delete=models.CASCADE, related_name="vendor_images")

    def __str__(self):
        return self.vendor.name
    

class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Storage(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Product(AbstractModel):
    name = models.CharField(max_length=50)
    vendor_id = models.ForeignKey('Vendor' , related_name= 'vendor_id' , on_delete= models.CASCADE)
    category_id = models.ForeignKey('ProductCategory' , related_name= 'category_id' , on_delete= models.CASCADE)


    def __str__(self): 
        return self.name
    

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')
    product = models.ForeignKey('product.ProductVersion', on_delete=models.CASCADE, related_name="images")
    
    def __str__(self):
        return self.product.product_id.name
    

class ProductVersion(AbstractModel):
    product_id = models.ForeignKey('Product' , related_name='product_id' , on_delete=models.CASCADE)
    price = models.FloatField()
    old_price = models.FloatField(null= True , blank= True)
    description = models.TextField()
    slug = models.SlugField('slug' , max_length=150 , null= True , blank=True)
    stock = models.IntegerField(default= 0)
    color_id = models.ForeignKey('Color' , related_name='color_id' , on_delete=models.CASCADE , verbose_name='Color' , null=True, blank=True)
    storage_id = models.ForeignKey('Storage' , related_name='storage_id' , on_delete=models.CASCADE , verbose_name='Storage' , null= True , blank = True)
    platform_id = models.ForeignKey('Platform' , related_name='platform_id' , on_delete=models.CASCADE , verbose_name= 'Platform' , null=True , blank=True)
    thumbnail = models.ImageField(verbose_name= 'Thumbnail' , null= True , blank= True)
    video_url = models.CharField(max_length=255, verbose_name= 'video' , null= True , blank= True)



    def __str__(self):
        return self.product_id.name
    
    @property
    def get_absolute_url(self, **kwargs):
        return reverse_lazy('product:productpage' , kwargs= {'slug':self.slug})
    
    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''

        return url

    @property
    def discount(self):
        return int (100 - (((self.price) / (self.old_price)) * 100))


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(ProductCategory , related_name='parent_category' , on_delete= models.CASCADE ,verbose_name= 'Parent Category' , null= True , blank= True)


class Platform(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.name


class Review(AbstractModel):
    user = models.ForeignKey(User , on_delete  = models.CASCADE , blank = True , null= True)
    product_version = models.ForeignKey(ProductVersion , on_delete= models.CASCADE , related_name='comments')
    content = models.CharField(max_length=255 , null = True , blank= True)


    def __str__(self) -> str:
        return f'{self.user.get_full_name()} - {self.content} - {self.product_version.product_id}'
    


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductVersion , related_name= 'wishlist_product')

    def __str__(self):
        return f"Wishlist of {self.user.first_name} {self.user.last_name}"