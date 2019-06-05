# custodes-app/modulos/campos.py
import re
# Define as regras para pegar a combinação de palavras para pegar o texto correto

def Captura(arquivo):
    
    # Ainda não sabemos o nome do responsavel paara realizar a pesquisa do script vinculado, então vamos deixar a
    # váriavel vazia. 
    responsavel=""
    # Selecione o campo da primeira ocorrência até a última, e os extraia.
    campos = [
        "^(?=Solicitação|Incidente).+?(?=Em)",  "(?=Status).+?(?=Ativo:)", "(?=Usuário afetado:).+?(?=,)",
        "(?=Responsável:).+?(?=,)", "(?=Grupo atribuído:).+?(?=Nível)","(?=Área da solicitação:).+?(?=Causa)", 
        "(?=Item de configuração).+?(?=ChargeBack)", "(?=Descrição).+?(?=Histórico)",
        "(?=Script).+?(?="+responsavel+"|Pai)", "(?=Encerrar).+?(?=System_AHD_generated,)" ]
    # Armazena todos os campos coletados para formatação do chamado (em forma de lista)
    info_chamados = []
    # Pega o total de chamado para determinar quantas vezes será realizada a consulta
    total_de_chamados = re.compile('Incidente: \d{6,}|Solicitação: \d{6,}',re.MULTILINE+re.DOTALL) 
    total_de_chamados = len(total_de_chamados.findall(arquivo))
    # Usado para controle
    loop = 0
    # Realizada a pesquisa usando número de chamados encontrados e salva na variavel info_chamados
    for chamado in range(total_de_chamados):  
        for campo in campos:
            regex = re.compile(campo,re.MULTILINE+re.DOTALL) 
            try:
              loop+=1
              info_chamados.append(regex.search(arquivo).group()) 
              if loop is 3:
                 responsavel = regex.search(arquivo).group()
            finally:
                 info_chamados.append("N/A")
                       
