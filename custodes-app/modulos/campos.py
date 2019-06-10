# custodes-app/modulos/campos.py
import re
# Define as regras para pegar a combinação de palavras para pegar o texto correto
def Captura(arquivo):
   # Selecione o campo da primeira ocorrência até a última, e os extraia.
   campos = ["(?=Solicitação:|Incidente:).+?(?=Em)", "(?=Status:).+?(?=Ativo:)", "(?=Usuário afetado:).+?(?=,)",
           "(?=Responsável:).+?(?=,)", "(?=Grupo atribuído:).+?(?=Nível)","(?=Área do incidente:|Área da solicitação:).+?(?=Item)", 
        "(?=Item de configuração:).+?(?=ChargeBack)", "(?=Descrição:).+?(?=Interrupção|Histórico)",
        "(?=Script).+?(?=Pai)", "(?=Encerrar).+?(?= pm | am |Pai|System_AHD_generated,)" ]
   # Armazena todos os campos coletados para formatação do chamado (em forma de lista)
   info_chamados = []
   # Captura
   for campo in campos:
       regex = re.compile(campo,re.MULTILINE+re.DOTALL)
       info_chamados.append(regex.findall(arquivo))
   
   return info_chamados

