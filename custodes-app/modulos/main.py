# custodes-app/modulos/main
import re
from django import forms


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
        
        # Ainda não sabemos o nome do responsavel paara realizar a pesquisa do script vinculado, então vamos deixar a
        # váriavel vazia. 
        responsavel=""
        # Selecione o campo da primeira ocorrência até a última, e os extraia.
        campos = [
        "(?=Solicitação).+?(?=m)", "(?=Incidente).+?(?=m)", "(?=Status).+?(?=Ativo:)", "(?=Usuário afetado:).+?(?=,)",
        "(?=Responsável:).+?(?=,)", "(?=Grupo atribuído:).+?(?=Nível)", "(?=Grupo atribuído:).+?(?=Nível)",
        "(?=Área da solicitação:).+?(?=Causa)", "(?=Item de configuração).+?(?=ChargeBack)", "(?=Descrição).+?(?=Histórico)",
        "(?=Script).+?(?="+responsavel+")", "(?=Encerrar).+?(?=System_AHD_generated,)" ]
         
        # Usado para controle
        loop = 0
        for campo in campos:
           re.search(campo,palavras,re.MULTILINE,re.DOTALL)
           loop+=1
           if loop is 3:
            responsavel = re.search(
        
       
