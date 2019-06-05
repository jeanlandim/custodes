# custodes-app/modulos/pegarelatorio.py
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
