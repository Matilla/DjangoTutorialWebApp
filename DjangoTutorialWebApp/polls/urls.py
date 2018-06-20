'''
Created on Jun 18, 2018

@author: Administrator
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]