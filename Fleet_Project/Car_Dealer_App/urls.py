from django.urls import path,include
from Car_Dealer_App.views import *
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^index/$', index, name='index'),
    re_path(r'^login/$', login, name='login'),
    
]