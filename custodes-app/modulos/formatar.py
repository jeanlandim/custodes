# custodes-app/modulos/formatar.py
def Formatar(info_chamados):
    # URL para o link direto de determinado chamado no
    # CA
    url = 'http://contas.tcu.gov.br/CAisd/pdmweb.exe?OP=SEARCH+FACTORY=cr+SKIPLIST=1+QBE.EQ.ref_num='
    # Retira os caracteres "[","]","'"
    caracteres_indesejados = ["[","]","\'"]
    # Campos em negrito
    campos_negrito = ["Usuário afetado","Responsável","Área da solicitação","Item de configuração","Descrição","Status","Grupo atribuído","Área do incidente"]
    # Dados limpos
    dados_limpos = []
    for texto_cru in info_chamados:
        texto_cru = str(texto_cru)
        for caracter in caracteres_indesejados:
            texto_cru = texto_cru.replace(caracter,"")

        texto_cru = texto_cru.replace(r"\t"," ")
        texto_cru = texto_cru.replace(r"\r\n","<br>")

        if texto_cru.split(":")[0] == "Incidente" or texto_cru.split(":")[0] == "Solicitação":
           numero_do_chamado = texto_cru.split(":")[1]
           numero_do_chamado = numero_do_chamado.replace(" ","")
           texto_cru = "<a href="+url+numero_do_chamado+">"+texto_cru+"</a>"

        for campos in campos_negrito: 
            if texto_cru.split(":")[0] == campos:
               texto_cru = "<i>"+texto_cru+"</i>"

        dados_limpos.append(texto_cru)

    return dados_limpos

