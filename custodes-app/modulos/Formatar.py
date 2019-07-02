class Formatar():
      ''' Formata o chamado que já foi capturado e extraido. No momento há dois tipos de formatos que serão utilizados: HTML e JSON. '''
      def __init__(self):
         self.Url = "http://contas.tcu.gov.br/CAisd/pdmweb.exe?OP=SEARCH+FACTORY=cr+SKIPLIST=1+QBE.EQ.ref_num="
         self.CamposEmNegrito = ["Usuário afetado","Responsável","Área da solicitação", "Item de configuração","Descrição","Status","Grupo atribuído", 
                                "Área do incidente","Script vinculado","Encerrar chamado", "Registrar Comentário"]
         self.CaracteresIndesejados = ["[","]","\'"]
         self.Substituir = ["\t","\r\n","Script vinculado","Registrar comentário","Encerrar chamado","Causa raiz:","Área do incidente","Área da solicitação"]
         self.Substitutos = [" "," ","Script vinculado:","Registrar comentário:","Encerrar chamado:","","Tipo do incidente","Tipo da solicitação"]     

        ''' Formata o relatório (já tratado) em HTML ou JSON. (No futuro poderá haver outras opçções '''    
      def Formatacao(RelatorioCru):
            DadosLimpos = PreFormatacao(RelatorioCru)
            NovosDadosEmJSON = {}

            ''' Pré formate o relatório tirando caracters indesejados. '''
            def PreFormatacao(RelatorioCru):
                DadosLimpos = []
                CaracteresIndesejados = self.CaracteresIndesejados
                Substituir = self.Substituir
                Substitutos = self.Substitutos
           
                for TextoCru in RelatorioCru:
                    TextoCru = str(TextoCru) 
                    for Caracter in CaracteresIndesejados:
                        TextoCru = TextoCru.replace(Caracter,"")
                    for Indice in range(len(Substituir)): 
                        TextoCru = TextoCru.replace(Substituir[Indice],Substitutos[Indice])
                    DadosLimpos.append(TextoCru)
                    return(DadosLimpos)
     
            def HTML(self):
            ''' Pega o relatório e o formate em HTML. '''
                NovosDadosEmHTML = []
                for Dados in DadosLimpos:
                    Dados = str(Dados)
                    ''' Gera o relatório em HTML ''' 
                    if Tipo is Tipos[0]:
                       for Campos in self.CamposEmNegrito: ''' transforma tais campos em negrito, utilizando o tag <b> '''
                           if Dados.split(":")[0] == Campos:
                              Dados = Dados.replace(Campos,"<b>"+Campos+"</b>") 

                           if Dados.split(":")[0] == "Incidente" or Dados.split(":")[0] == "Solicitação": '''  transforma em hyperlink o campo referente ao chamado '''
                              NumeroDoChamado = Dados.split(":")[1]
                              NumeroDoChamado = NumeroDoChamado.replace(" ","")
                              Dados = "<a href="+UrlDoServiceDesk+NumeroDoChamado+" target=\"_blank\">"+Dados+"</a>" 

                              NovosDadosEmHTML.append(Dados)
                     return(NovosDadosEmHTML)
            def JSON(self):
            ''' 
