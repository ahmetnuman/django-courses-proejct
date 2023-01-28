from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("anasayfa")

def kurslar(request):
    return HttpResponse("kurs listesi")

# Create your views here.
