# custodes-app/modulos/campos.py
# Importa a biblioteca de regex
import re
# Para debug do modulo
def debug(_debug):
    debug = open('debug.txt','w')
    debug.write(_debug)
    debug.close()
# Define as regras para pegar a combinação de palavras para pegar o texto correto
def Captura(Relatorio):
    # Selecione o campo da primeira ocorrência até a última, e os extraia.
    # Esses são os campos que são imutáveis, ou seja, todos os chamados os têm.
    campos_padroes = ["(?=Solicitação:|Incidente:).+?(?=Em)",
                     "(?=Status:).+?(?=Ativo:)",
                     "(?=Usuário afetado:).+?(?=,)",
                     "(?=Responsável:).+?(?=,)",
                     "(?=Grupo atribuído:).+?(?=Nível)",
                     "(?=Área do incidente:|Área da solicitação:).+?(?=Item)",
                     "(?=Item de configuração:).+?(?=ChargeBack)",
                     "(?=Descrição:).+?(?=Interrupção|Histórico)",
                     "(?=Script).+?(?=^$)",
                     "(?=Encerrar).+?(?=Pai:)",
                     "(?:Registrar comentário).+?(?=Não resolvido, fechado)"]
    # Delimitador de chamado, que será usada para fazer a fatia do chamado
    delimitador_chamado = ["(?=Solicitação:|Incidente:).+?(?=SLA)"]

    # Pega o total de chamados para criação dos dicionários, os quais conteram os atributos de cada chamado   
    total_de_chamados = len(re.findall(campos_padroes[0],Relatorio,re.MULTILINE+re.DOTALL))

    # Cria o dicionário 'chamado', para guardar nas chaves (que serão representadas por números) e irão conter as informações
    # do chamado.
    chamado = {}
    for chave in range(total_de_chamados):
        chamado[chave] = [] # Cria lista para cada chamados
    # Cria lista para guardar os chamados fatiados
    chamados_fatiados = []
    # Fatia os chamados
    for iteracao in range(total_de_chamados):
        chamados_fatiados.append(re.findall(delimitador_chamado,Relatorio,re.MULTILINE+re.DOTALL))
        # Passa para 'campo' a expressão regular para captura dos campos (padrões) 
        for campo in campos_padroes:
            # Compila a expressão regular que define o campo
            exp_reg = re.compile(campo,re.MULTILINE+re.DOTALL)
            for _campo in exp_reg.findall(chamados_fatiados[iteracao]): # Coloca em cada chamado o campo capturado
                chave = iteracao
                chamado[chave].append(_campo) 
        iteracao+=1 
    
    debug(str(chamado)) 
