from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def saludar(request):
    return HttpResponse(" Te amo !")

def bicha(request):
    return HttpResponse("pene")