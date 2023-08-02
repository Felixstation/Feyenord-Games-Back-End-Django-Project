from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render , redirect
from product.models import Platform , ProductVersion
from core.models import AdvertImage
from .forms import SubscribeForm , ContactForm
from django.views.generic import ListView , CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.forms.models import BaseModelForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

# def index(request):
#     platform = Platform.objects.all()
#     advert = AdvertImage.objects.all()
#     product = ProductVersion.objects.filter()[:8]
#     form = SubscribeForm()
#     if request.method == 'POST':
#         form = SubscribeForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('core:index')
#     context = {
#         'platform' : platform,
#         'advert':advert,
#         'product':product,
#         'form': form
#     }

#     return render(request , 'index.html' , context)


class IndexListView(ListView):
    model = ProductVersion
    template_name = 'index.html'
    context_object_name = 'product_list'
    queryset = ProductVersion.objects.filter().order_by('-created_at')[:8]

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['platform'] = Platform.objects.all()
        context['advert_image'] = AdvertImage.objects.all()
        context['games'] = ProductVersion.objects.filter(product_id__category_id__name = 'Games')[:4]
        context['consoles'] = ProductVersion.objects.filter(product_id__category_id__name = 'Consoles')
        context['accessories'] = ProductVersion.objects.filter(product_id__category_id__name = 'Accessories')


        return context


def about(request):
    return render(request , 'about-page.html')

class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('core:contact')
    def form_valid(self , form = BaseModelForm):
         message = f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']} - {form.cleaned_data['email']} - {form.cleaned_data['phone']}"
         subject = 'Someone Want Contact Us!'
         from_email = 'feridhuseynli13@gmail.com'
         to_email = ["feridhuseynli13@gmail.com"]
         send_mail(subject, message, from_email, to_email)
         messages.success(self.request , _('Your Information Succesfully Sent!'))
         return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        messages.error(self.request , _('Please Check Your Information!'))
        return super().form_invalid(form)

# def consoles(request):
#     consoles = ProductVersion.objects.filter(product_id__category_id__name= 'Consoles').all()

#     context = {
#         'consoles' : consoles
#     }
#     return render (request , 'consoles.html' , context)


class ConsolesListView(ListView):
    model = ProductVersion
    template_name = 'consoles.html'
    queryset = ProductVersion.objects.filter(product_id__category_id__name =  'Consoles').all()
    context_object_name = 'consoles'


class GameListView(ListView):
    model = ProductVersion
    template_name = 'games.html'
    context_object_name = 'games'
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        id=self.kwargs["id"]
        context['games'] = ProductVersion.objects.filter(platform_id = id).all()
        return context


class AccessoriesListView(ListView):
    model = ProductVersion
    template_name = 'accessories.html'
    context_object_name = 'accessories'
    queryset = ProductVersion.objects.filter(product_id__category_id__name= 'Accessories').all()

def faq(request):
    return render(request , 'faq.html' )

# def games(request , id):
#     games = ProductVersion.objects.filter(platform_id = id).all()

#     context = {
#         'games': games
#     }
    
#     return render(request , 'games.html' , context)


# def accessories(request):
#     accessories = ProductVersion.objects.filter(product_id__category_id__name= 'Accessories').all()

#     context = {
#         'accessories' : accessories,
#     }
#     return render (request , 'accesories.html' , context)




def search(request):
    return render(request , 'search.html')


# custom 404 view
def custom_404(request, exception):
    return render(request, 'core:404.html', status=404)


def quick_view(request):
    product = ProductVersion.objects.all()

    context = {
        'product': product
    }

    return render(request , 'base.html' , context)

