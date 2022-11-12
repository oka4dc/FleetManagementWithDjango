from django.urls import path,include
from django.conf.urls import url
from Home.views import home_page
from Car_Dealer_App import *
from Customer_Portal import *

urlpatterns = [
    url(r'^$',home_page),
]
