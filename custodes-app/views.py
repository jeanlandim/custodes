# custodes-app/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .modulos.main import PegaRelatorio
from tempfile import NamedTemporaryFile
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
    dados = request.POST.get('relatorio')
   # arquivo_temp_cru = TemporaryFile(mode='w+t') # Cria um arquivo temporário escrito, o formulário cru
   
    # Pega da primeira ocorrência até a última e grava no arquivo 
    # Escreve no arquivo tempoário os dados crus
   # arquivo_temp.writelines(dados)
    return render(request,'relatorio_final.html',{'data':dados}) # os insere na nova página
