# custodes-app/modulos/campos.py
import re
# Define as regras para pegar a combinação de palavras para pegar o texto correto

def Captura(arquivo):
    
    # Ainda não sabemos o nome do responsavel paara realizar a pesquisa do script vinculado, então vamos deixar a
    # váriavel vazia. 
    responsavel=""
    # Selecione o campo da primeira ocorrência até a última, e os extraia.
    campos = [
        "Solicitação: \d{6,} | Incidente: \d{6,}", "(?=Status).+?(?=Ativo:)", "(?=Usuário afetado:).+?(?=,)",
        "(?=Responsável:).+?(?=,)", "(?=Grupo atribuído:).+?(?=Nível)","(?=Área da solicitação:).+?(?=Causa)", 
        "(?=Item de configuração).+?(?=ChargeBack)", "(?=Descrição).+?(?=Histórico)",
        "(?=Script).+?(?="+responsavel+"|Pai)", "(?=Encerrar).+?(?=System_AHD_generated,)" ]
    # Armazena todos os campos coletados para formatação do chamado (em forma de lista)
    info_chamados = []
   
    loop = 0
    for campo in campos:
        regex = re.compile(campo,re.MULTILINE+re.DOTALL) 

        numero_de_chamados = len(re.findall(arquivo))
        numero_de_chamados = numero_de_chamados - 1
        chave = "chamado_"+str(numero_de_chamados)
        # pega as solicitações        
        if loop is 0:
            info_chamados[chave].append(
