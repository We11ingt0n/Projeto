from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    
   return  render(request,'SGAE\login.html')

def home(request):
    
   return  HttpResponse('Home')

def alunos(request):
    
   return  HttpResponse('Alunos')

def financeiro(request):
    
   return  HttpResponse('Financeiro')

