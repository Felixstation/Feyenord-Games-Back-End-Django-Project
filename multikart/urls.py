"""multikart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include , re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , include('product.api.urls')),
    path('auth/' , include('account.api.urls')),
    path("unicorn/", include("django_unicorn.urls")),
    path('' , include('product.urls')),
    path('' , include('account.urls')),
    path('' , include('core.urls')),
    path('' , include('order.urls')),
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

handler404 = 'core.views.custom_404'


urlpatterns += i18n_patterns(
    re_path(r'^rosetta/', include('rosetta.urls')),
    path('i18n/' , include('django.conf.urls.i18n')),
    path('' , include('product.urls')),
    path('' , include('account.urls')),
    path('' , include('core.urls')),
    path('' , include('order.urls')),
)