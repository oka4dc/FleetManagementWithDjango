from django.urls import path,include
from django.urls import include, re_path
from Home.views import home_page
from Car_Dealer_App import *


urlpatterns = [
    re_path(r'^$', home_page),
]