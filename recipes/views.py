from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse


# HTTP REQUEST
def home(request):
    return HttpResponse('Home')
    # return HTTP Response
# Create your views here.
def _contato(request):
    return HttpResponse('Contato')

def sobre(response):
    return HttpResponse('Sobre')