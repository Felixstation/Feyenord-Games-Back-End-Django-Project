from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from .forms import RegisterForm , LoginForm , UserProfileUpdateForm
from django.contrib.auth import login as django_login, authenticate, logout as django_logout , get_user_model , views as auth_views
from django.contrib.auth.views import PasswordChangeView , LoginView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from account.tokens import account_activation_token
from django.utils.http import urlsafe_base64_decode
from account.tokens import account_activation_token
from django.utils.encoding import force_str
from django.views.generic import ListView , CreateView

User = get_user_model()

# def login(request):
#     next_page = request.GET.get('next' , reverse_lazy('core:index'))
#     form = LoginForm()

#     if request.method == 'POST':
#         form = LoginForm(data = request.POST)
#         if form.is_valid():
#             user = authenticate(request=request , username = form.cleaned_data['username'] , password = form.cleaned_data['password'])
#             if not user:
#                 messages.add_message(request , messages.ERROR , 'User Not Found!')
#             else:
#                 django_login(request, user)

#                 return redirect(next_page)
#     context = {
#         'form': form
#     }
#     return render(request , 'login.html' , context)


class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm


    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        
        messages.error(self.request , 'Please Check Your Login Information! If password was forgotten, click Forget Password Button') 

        return super().form_invalid(form)
    


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data = request.POST ,files = request.FILES)

        if form.is_valid():
            user = form.save(commit= False)
            print(user)
            current_site = get_current_site(request)
            subject = 'Activate Your Multikart Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account:account_activation')

    context = {
        'form': form

    }

    return render(request , 'register.html' , context)

def logout(request):
    django_logout(request)
    return redirect('core:index')



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'change-password.html'
    success_url = reverse_lazy('account:success-password')

@login_required
def SuccessPassword(request):
    return render(request, 'password-success.html')

def forget_pwd(request):
    return render(request , 'forget_pwd.html')


def activation_email(request):
    return render(request , 'activation_account.html')





class ChangeProfileView(CreateView):
    template_name = 'change-profile.html'
    context_object_name = 'change_profile'
    form_class = UserProfileUpdateForm
    success_url = reverse_lazy('account:profile')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)
        


def vendor_profile(request):
    return render(request , 'vendor-profile.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('account:login')
    else:
        return redirect('account:register')
    
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST , request.FILES , instance=request.user)
        if form.is_valid():
            messages.success(request , 'Profile Updated Succesfully!')
            form.save()
        return redirect(reverse_lazy('account:profile'))
    else:
        form = UserProfileUpdateForm(instance=request.user)
    context = {
            'form' : form
        }
    return render(request,'profile.html' ,context)
