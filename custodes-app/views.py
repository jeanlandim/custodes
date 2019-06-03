# custodes-app/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .modulos.main import PegaRelatorio, Campos
# Create your views here

# Página inicial do site
def Index(request):
    if request.method == 'POST': 
        form = PegaRelatorio(request.POST)
        if form.is_valid():
           return HttpResponseRedirect('coletando/') 
    else:
            form = PegaRelatorio()
    return render(request,'index.html',{'form':form}) 
# Grava os dados crus, gerados pelo formulário, o formate na maneira correta e o abre
# em seguida na nova requisição
def Coleta(request):
    # Coleta os dados do relatório gerado na página inicial do app
    dados = str(request.POST.get('relatorio'))
    arquivo = open('saida.txt','a')
    x = dados.replace('\r\n',' ')
    x = x.replace('\t',' ')
    arquivo.write(Campos.Captura(x))
    arquivo.close()
    return render(request,'relatorio_final.html',{'data':dados}) # os insere na nova página
