from django.urls import path , re_path , include
from account.views import *
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login' , UserLoginView.as_view() , name = 'login'),
    path('register' , register , name = 'register'),
    path('logout' , logout , name = 'logout'),
    path('profile' , profile , name = 'profile'),
    path('change-profile' , ChangeProfileView.as_view() , name = 'change_profile'),
    path('vendor-profile' , vendor_profile , name = 'vendor_profile'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
        activate, name='activate'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('change-password/' , PasswordsChangeView.as_view() , name='change_password'),
    path('activation-sent/' , activation_email , name='account_activation'),
    path('change-success' , SuccessPassword , name= 'success-password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = "password_reset.html",
                                                                 success_url = reverse_lazy('account:password_reset_done'),
                                                                 email_template_name= 'password_reset_email.html'), name ='password-reset'),
    path('password-reset/done/  ', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_done.html"), name ='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_confirm.html"), name ='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),


    
    
]
