from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("anasayfa")

def hakkimizda(request):
    return HttpResponse("Hakkımızda")

def iletisim(request):
    return HttpResponse("iletisim bilgileri")        

# Create your views here.
