# custodes-app/urls.py
from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [
        path('',Index,name='Index'), # Sem caminho após a URL principal
                                     # vá para LoginUsuario da views.py
        path('coletando/',Coleta,name="Coleta") 
        
]



