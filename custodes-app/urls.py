# custodes-app/urls.py
from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
        path('',Index,name='Index'), 
        path('coletando/',Coleta,name="Coleta") 
        
]



