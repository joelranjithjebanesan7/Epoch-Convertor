from django.conf.urls import url
from epoch import views 
from django.conf.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    url(r'^epoch/$', views.epoch_convertor, name = 'epoch-convertor'),
    
    ]