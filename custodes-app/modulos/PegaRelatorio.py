from django import forms
class PegaRelatorio(forms.Form):
    relatorio = forms.CharField(
                  widget = forms.Textarea(
                  attrs = {'placeholder': 'Cole aqui o relatório gerado pela CA'}),label='')
 
