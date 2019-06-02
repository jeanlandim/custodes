# custodes-app/forms.py

from django import forms

class Relatorio(forms.Form):
    relatorio = forms.CharField(
            widget = forms.Textarea(attrs = {'placeholder': 'Cole aqui o relatório gerado pela CA'}),label='')

    def limpa(self):
        dados_limpados = super(Relatorio, self).clean()
        relatorio = dados_limpados('relatorio')
        if not relatorio:
            raise forms.ValidationErro("É necessário que você colo o relatório gerado")

