from django.shortcuts import render
from django.http import HttpResponse

def kurslar(request):
    return HttpResponse("kurs listesi")
def details(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} kursu detayları")  
def getCoursesByCategory(request, category_name):
    text = ""
    if category_name == "programlama":
        text = "programlama kategorisine ait kurslar"
    elif category_name == "web-gelistirme":
        text = "web gelistirme kategorisine ait kurslar"
    else:
        text = "Bu kategori bizde bulunmamaktadır."        
    return HttpResponse(text)       

def getCoursesByCategoryId(request, category_id):
    return HttpResponse(category_id)



# Create your views here.
