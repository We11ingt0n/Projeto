from django.http import HttpResponse
from django.urls import path

from SGAE.views import alunos, financeiro, home, login

urlpatterns = [
    path('', login),
    path('home/', home),
    path('alunos/', alunos),
    path('financeiro/', financeiro)
]