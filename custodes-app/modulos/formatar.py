# custodes-app/modulos/formatar.py
def Formatar(info_chamados):
    # URL para o link direto de determinado chamado no CA
    url = 'http://contas.tcu.gov.br/CAisd/pdmweb.exe?OP=SEARCH+FACTORY=cr+SKIPLIST=1+QBE.EQ.ref_num='
    # Retira os caracteres "[","]","'" da lista
    caracteres_indesejados = ["[","]","\'"]
    # Define campos que irão estar em negrito
    campos_negrito = ["Usuário afetado","Responsável","Área da solicitação",
            "Item de configuração","Descrição","Status","Grupo atribuído",
            "Área do incidente","Área da solicitação","Script vinculado","Encerrar chamado",
            "Registrar Comentário"]
    # Substitui tais strings em ordem na lista abaixo pelas strings (também em ordem) da lista subjacente
    substituir = ["\t","\r\n","Script vinculado","Registrar comentário","Encerrar chamado"]
    substitutos = [" "," ",substituir[2]+":",substituir[3]+":",substituir[4]+":"]
    # Dados limpos
    dados_limpos = []
    for texto_cru in info_chamados:
        texto_cru = str(texto_cru) # Define texto_cru como string
        # Apaga os caracteres indesejados, gerados pelo método findall (do módulo re)
        for caracter in caracteres_indesejados:
            texto_cru = texto_cru.replace(caracter,"")
        # Substitui algumas strings 
        for indice in range(len(substituir)): 
            texto_cru = texto_cru.replace(substituir[indice],substitutos[indice])
        # Cria o link para o chamado de acordo com o número do mesmo
        if texto_cru.split(":")[0] == "Incidente" or texto_cru.split(":")[0] == "Solicitação":
           numero_do_chamado = texto_cru.split(":")[1]
           numero_do_chamado = numero_do_chamado.replace(" ","")
           texto_cru = "<a href="+url+numero_do_chamado+">"+texto_cru+"</a>"
        # Define tais campos em negrito
        for campos in campos_negrito: 
            if texto_cru.split(":")[0] == campos:
               texto_cru = texto_cru.replace(campos,"<b>"+campos+"</b>")
        # No final do laço incrementa o dicionário
        dados_limpos.append(texto_cru)
    
    return dados_limpos
