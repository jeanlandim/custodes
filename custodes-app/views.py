# custodes-app/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .modulos.custodesapp import CustodesApp
# Página inicial do site
def Index(request):
    if request.method == 'POST': 
        Formulario = CustodesApp.PegaRelatorio(request.POST)
        if Formulario.is_valid():
           return HttpResponseRedirect('coletando/') 
    else:
            Formulario = CustodesApp.PegaRelatorio()
    return render(request,'index.html',{'form':Formulario}) 

# Grava os dados crus, gerados pelo formulário, o formate na maneira correta e o abre
# em seguida na nova requisição
def Coleta(request):
    # Coleta os dados do relatório gerado na página inicial do app
    Dados = request.POST.get('relatorio')
    Chamados = CustodesApp.Formatar(CustodesApp.Captura(Dados))
    return render(request,'relatorio_final.html',{'chamados':Chamados}) # os insere na nova página
