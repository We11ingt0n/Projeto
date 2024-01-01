from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    
   return  HttpResponse('Login')

def home(request):
    
   return  HttpResponse('Home')

def alunos(request):
    
   return  HttpResponse('Alunos')

def financeiro(request):
    
   return  HttpResponse('Financeiro')

