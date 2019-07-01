# custodes-app/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .os.formatar import Formatar
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
    chamados = Formatar(Captura(dados))
    chamados = Captura(dados)
    return render(request,'relatorio_final.html',{'chamados':chamados}) # os insere na nova página
