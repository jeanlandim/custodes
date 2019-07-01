# custodes-app/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .modulos.custodesapp import CustodesApp
from .modulos.custodesapp import PegaRelatorio
# Página inicial do site
def Index(request):
   Formulario = PegaRelatorio(request.POST)
   if request.method == 'POST': 
      if Formulario.is_valid():
           return HttpResponseRedirect('coletando/') 
   return render(request,'index.html',{'form':Formulario}) 

# Grava os dados crus, gerados pelo formulário, o formate na maneira correta e o abre
# em seguida na nova requisição
def Coleta(request):
    # Coleta os dados do relatório gerado na página inicial do app
    Dados = request.POST.get('relatorio')
    Chamados = CustodesApp().Formatar(CustodesApp().Captura(Dados))
    return render(request,'relatorio_final.html',{'chamados':Chamados}) # os insere na nova página
