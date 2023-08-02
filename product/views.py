from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render , redirect , HttpResponse , get_object_or_404
from .models import ProductVersion , ProductImage , Wishlist , ProductCategory , Storage , Color , Product , Vendor
from django.views.generic import DetailView , ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from .forms import ReviewForm
from .tasks import export_data
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# def category_page(request):
#     return render(request , 'category-page.html')

# def product_page(request , id):
#     product = ProductVersion.objects.get(id = id)
#     product_image = ProductImage.objects.filter(product = product).all()
    
#     context = {
#         'product': product,
#         'product_images': product_image

#     }
    
#     return render(request , 'product-page.html' , context)


class ProductDetailView(DetailView , FormMixin):
    model = ProductVersion
    template_name = 'product-page.html'
    context_object_name= "productversion"
    form_class = ReviewForm
    queryset = ProductVersion.objects.all().order_by('created_at')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['new_products_1'] = ProductVersion.objects.all().order_by('-created_at')[:4]
        context['new_products_2'] = ProductVersion.objects.all().order_by('-created_at')[4::8]
        context['related_products'] = ProductVersion.objects.filter(product_id__category_id = self.get_object().product_id.category_id).all() 
        context['category'] = ProductCategory.objects.all()
 
        return context
    
    def get_success_url(self) -> str:
        return reverse_lazy( 'product:productpage' , kwargs = {'slug': self.object.slug} )
    
    def post(self , request , *args , **kwargs):
            self.object = self.get_object()
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
            
    def form_valid(self, form: any):
        form.instance.product_version = self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    


class AllProductView(ListView):
    model = ProductVersion
    template_name = 'category-page.html'
    context_object_name = 'all'


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['category'] = ProductCategory.objects.all()
        context['storage'] = Storage.objects.all()
        context['color'] = Color.objects.all()
        context['vendor'] = Vendor.objects.all()

        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        product = super().get_queryset()

        catid = self.request.GET.get('categories')
        colorid = self.request.GET.get('color')
        vendorid = self.request.GET.get('vendor')
        max_price = self.request.GET.get('max_price')
        min_price = self.request.GET.get('min_price')
         

        if catid :
            product = ProductVersion.objects.filter(product_id__category_id = catid).all()
        
        

        if colorid :
            product = ProductVersion.objects.filter(color_id = colorid).all()
        
        
        if vendorid :
            product = ProductVersion.objects.filter(product_id__vendor_id = vendorid).all()
        
  

        if min_price:
            product = ProductVersion.objects.filter(price__gte = min_price) 
        
        
        if max_price:
            product = ProductVersion.objects.filter(price__lte = max_price)



        return product



def export_view(request):
     export_data.delay()
     return HttpResponse('success')


@login_required
def wishlist_view(request):
    wishlist = Wishlist.objects.get_or_create(user=request.user)[0]
    items = wishlist.product.all()
    return render(request, 'wishlist.html', {'items': items})
    
    


@login_required
def add_to_wishlist(request, slug , **kwargs):
    product = ProductVersion.objects.get(slug = slug)
    wishlist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist.product.add(product)
    return redirect('product:wishlist_view')

   

@login_required
def remove_from_wishlist(request, slug):
    if request.user.is_authenticated:
        product = get_object_or_404(ProductVersion, slug=slug)
        wishlist = Wishlist.objects.get(user=request.user)
        messages.success(request, "Succesfully Removed!") 
        wishlist.product.remove(product)
    return redirect('product:wishlist_view')