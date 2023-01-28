from django.urls import path
from . import views


#http://127.0.0.1:8000 => anasayfa
#http://127.0.0.1:8000/home => anasayfa
#http://127.0.0.1:8000/anasayfa => anasayfa
#http://127.0.0.1:8000/kurslar => kurs listesi



urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('anasayfa/', views.home),
    path('kurslar/', views.kurslar),
    
]