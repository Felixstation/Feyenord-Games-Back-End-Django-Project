from django.urls import path
from core.views import *
app_name = 'core'


urlpatterns = [
    path('', IndexListView.as_view(), name = 'index'),
    path('about/', about , name = 'about') , 
    path('contact' , ContactView.as_view() , name = 'contact') , 
    path('faq' , faq , name = 'faq'),
    path('consoles' , ConsolesListView.as_view() , name = 'consoles'),
    path('games/<int:id>' , GameListView.as_view() , name = 'games'),
    path('accessories' , AccessoriesListView.as_view() , name= 'accessories'),
    path('search' , search , name = 'search' ),
]
    