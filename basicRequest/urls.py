from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, re_path

from . import views

app_name= 'servicio'

urlpatterns = [
    path('recive/', views.recive, name='recive'),
	path('view/', views.showData, name='show'),
	path('post/', views.postData, name='post'),
]