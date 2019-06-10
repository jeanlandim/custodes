# custodes - app / modulos / campos.py
import re
# Define as regras para pegar a combinação de palavras para pegar o texto correto
def Captura(arquivo):
    # Selecione o campo da primeira ocorrência até a última, e os extraia.
    campos = ["(?=Solicitação:|Incidente:).+?(?=Em)",
        "(?=Status:).+?(?=Ativo:)",
        "(?=Usuário afetado:).+?(?=,)",
        "(?=Responsável:).+?(?=,)",
        "(?=Grupo atribuído:).+?(?=Nível)",
        "(?=Área do incidente:|Área da solicitação:).+?(?=Item)",
        "(?=Item de configuração:).+?(?=ChargeBack)",
        "(?=Descrição:).+?(?=Interrupção|Histórico)",
        "(?=Script).+?(?=^$)",
        "(?=Encerrar).+?(?=Pai:)"
         ]
    # Armazena todos os campos coletados para formatação do chamado(em forma de lista)
    info_chamados = []
    # Captura
    for campo in campos:
        regex = re.compile(campo, re.MULTILINE + re.DOTALL)
        info_chamados.append(regex.findall(var))
	 a = 0
    chamados = []
    for i in info_chamados[0]:
        chamados.append(i + info_chamados[1][a] + info_chamados[2][a] + " " + info_chamados[3][a] + " " +
                info_chamados[4][a] + info_chamados[5][a] + info_chamados[6][a] + info_chamados[7][a] +
                info_chamados[8][a] + info_chamados[9][a])
	a += 1
    return (chamados)
