# custodes-app/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .modulos.Captura import Captura
from .modulos.Formatar import Formatar
from .modulos.PegaRelatorio import PegaRelatorio

''' Página inicial do app '''
def Index(request):
    if request.method == 'POST': 
       form = PegaRelatorio(request.POST)
       if form.is_valid():
          return HttpResponseRedirect('coletando/') 
    else:
       form = PegaRelatorio()
    return render(request,'index.html',{'form':form}) 

''' Grava os dados crus, gerados pelo formulário, o formate na maneira correta e o abre em seguida na nova requisição '''
def Coleta(request):
    
    ''' Coleta os dados do relatório gerado na página inicial do app '''
    Dados = request.POST.get('relatorio')
    
    ''' Captura os dados (do relatório) e extraía os campos '''
    def Capture(Dados):
        _Capture = Captura()
        return(_Capture.Captura(Dados))
    
    ''' Formate os dados extraidos do relatório e o formate '''
    def Formate(Dados):
        _Formate = Formatar()
        return(_Formate.Formatacao(Dados))
               
    ''' Pegue os dados capturados e logo em seguida o formate '''           
    Chamados = Formate(Capture(Dados))
    return render(request,'relatorio_final.html',{'chamados':Chamados}) # os insere na nova página
