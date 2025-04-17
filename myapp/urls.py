from django.contrib import admin
from django.urls import path,include
from myapp.views import  index,result
urlpatterns = [
    path('',index,name='index'),
    path('result/',result,name='result'),


]