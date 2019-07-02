class Formatar(self,RelatorioCru):
      ''' Formatar:
          Formata o chamado que já foi capturado e extraido. No momento há dois tipos de formatos que serão utilizados: HTML e JSON.
      '''
      def __init__(self):
         self.Url = "http://contas.tcu.gov.br/CAisd/pdmweb.exe?OP=SEARCH+FACTORY=cr+SKIPLIST=1+QBE.EQ.ref_num="
    
        def PreFormatacao(RelatorioCru):
            DadosLimpos = []
            CaracteresIndesejados = self.Substituicoes['CaracteresIndesejados']
            Substituir = self.Substituicoes['Substituir']
            Substitutos = self.Substituicoes['Substitutos']
            
            for TextoCru in RelatorioCru:
                TextoCru = str(TextoCru) 
                for Caracter in CaracteresIndesejados:
                    TextoCru = TextoCru.replace(Caracter,"")
                for Indice in range(len(Substituir)): 
                    TextoCru = TextoCru.replace(Substituir[Indice],Substitutos[Indice])
                DadosLimpos.append(TextoCru)

            return(DadosLimpos)
    
        def Formatacao(Tipo):
            DadosLimpos = PreFormatacao(RelatorioCru)
            Tipos = ["HTML","JSON"]
            NovosDadosEmHTML = []
            NovosDadosEmJSON = {}
            CamposEmNegrito = self.Substituicoes['CamposNegritos']

            for Dados in DadosLimpos:
                Dados = str(Dados)
                # gera o relatório em HTML
                if Tipo is Tipos[0]:
                     for Campos in CamposEmNegrito: # transforma tais campos em negrito, utilizando o tag <b> 
                          if Dados.split(":")[0] == Campos:
                             Dados = Dados.replace(Campos,"<b>"+Campos+"</b>") 

                          if Dados.split(":")[0] == "Incidente" or Dados.split(":")[0] == "Solicitação": # transforma em hyperlink o campo referente ao chamado
                             NumeroDoChamado = Dados.split(":")[1]
                             NumeroDoChamado = NumeroDoChamado.replace(" ","")
                             Dados = "<a href="+UrlDoServiceDesk+NumeroDoChamado+" target=\"_blank\">"+Dados+"</a>" 

                             NovosDadosEmHTML.append(Dados)
                     return(NovosDadosEmHTML)
 
