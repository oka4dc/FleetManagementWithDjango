from django.urls import include
from Customer_Portal.views import *
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^index/$', index, name='index'),
    re_path(r'^login/$', login, name='login'),
    re_path(r'^auth/$', auth_view, name='auth_view'),
    re_path(r'^logout/$', logout_view, name='logout_view'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^registration/$', registration, name='registyration'),
    #re_path(r'^search/$', login, name='search'),
]
