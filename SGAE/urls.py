from django.http import HttpResponse
from django.urls import path

from SGAE.views import home

urlpatterns = [
    path('', home),
   
]