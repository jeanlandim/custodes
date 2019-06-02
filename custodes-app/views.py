# custodes-app/views.py
from django.shortcuts import render
from django.http import HttpResponse 
from .form import Relatorio 

# Create your views here

# View para o index do site
def Index(request):
    if request.method == 'POST':
        form = Relatorio(request.POST)
        if form.is_valid():
            pass
    else:
            form = Relatorio()
    return render(request,'index.html',{'form':form}) 
