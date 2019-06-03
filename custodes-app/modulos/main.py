# custodes-app/modulos/main
from django import forms
import re

# PegaRelatorio
# Carrega o formulário da página inicial e o prepara para mandar para 
# o seu processamento
class PegaRelatorio(forms.Form):
    relatorio = forms.CharField(
    widget = forms.Textarea(
        attrs = {'placeholder': 'Cole aqui o relatório gerado pela CA'}),label='')
            # placeholder: Coloca o texto dentro textarea do formulário
    def limpa(self):
        dados_limpados = super(relatorio, self).clean()
        relatorio = dados_limpados('relatorio')
        if not relatorio:
            raise forms.ValidationError("É necessário que você cole o relatório gerado.")
# Define as regras para pegar a combinação de palavras para pegar o texto correto
class Campos():
    def Captura(palavras):
        if (re.search("(?=Solicitação).+?(?=m)",palavras)):
            return re.search("(?=Solicitação).+?(?=m)",palavras).group()
        if(re.search("(?=Incidente).+?(?=m)",palavras)):
            return re.search("(?=Incidente).+?(?=m)",palavras).group()
        if(re.search("(?=Status).+?(?=Ativo:)",palavras)):
            return re.search("(?=Status).+?(?=Ativo:)",palavras).group()
        if(re.search("(?=Usuário afetado:).+?(?=,)",palavras)):
            return re.search("(?=Usuário afetado:).+?(?=,)",palavras).group()
        if(re.search("(?=Responsável:).+?(?=,)",palavras)):
            # Pega o primeiro nome do responsável para ser usado futuramente 
            # no if do 'Script vinculado'
            _responsavel = re.search("(?=Responsável:).+?(?=,)",palavras).group()
            responsavel = _responsavel.split(" ")[1]
            return re.search("(?=Responsável:).+?(?=,)",palavras).group()
        if(re.search("(?=Grupo atribuído:).+?(?=Nível)",palavras)):
            return re.search("(?=Grupo atribuído:).+?(?=Nível)",palavras).group()
        if(re.search("(?=Área da solicitação:).+?(?=Causa)",palavras)):
            return re.search("(?=Área da solicitação:).+?(?=Causa)",palavras).group()
        if(re.search("(?=Item de configuração).+?(?=ChargeBack)",palavras)):
            return re.search("(?=Item de configuração).+?(?=ChargeBack)",palavras).group()
        if(re.search("(?=Descrição).+?(?=Histórico)",palavras)):
            return re.search("(?=Descrição).+?(?=Histórico)",palavras).group()
        if(re.search("(?=Script).+?(?=)",palavras)):
            return re.search("(?=Script).+?(?="+responsavel+")",palavras).group()
        if(re.search("(?=Encerrar).+?(?=System_AHD_generated,)",palavras)):
            return re.search("(?=Encerrar).+?(?=System_AHD_generated,)",palavras).group()
