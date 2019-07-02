import re, json
class Captura():

    def __init__(self):
        self.CamposPadroes = ["(?=Solicitação:|Incidente:).+?(?=Em)", "(?=Status:).+?(?=Ativo:)", "(?=Usuário afetado:).+?(?=,)", "(?=Responsável:).+?(?=,)",
                              "(?=Grupo atribuído:).+?(?=Nível)","(?=Área do incidente:|Área da solicitação:).+?(?=Item)", "(?=Item de configuração:).+?(?=ChargeBack)",
                              "(?=Descrição:).+?(?=Interrupção|Histórico)",
                              "Script(?!.*Script).+?(?=Registrar comentário|Encerrar chamado)",
                              "(?=Encerrar).+?(?=Pai:)", "Registrar comentário(?!.*Registrar comentário).+?(?=, fechado)"]
        self.DelimitadorDeChamados = "(?=Solicitação:|Incidente:).+?(?=Tipo de serviço:)"
        self.CaracteresIndesejados = ["[","]","\'"],
        self.CamposNegritos = ["Usuário afetado","Responsável","Área da solicitação", "Item de configuração","Descrição","Status","Grupo atribuído", 
                               "Área do incidente","Script vinculado","Encerrar chamado", "Registrar Comentário"], 
        self.Substituir = ["\t","\r\n","Script vinculado","Registrar comentário","Encerrar chamado","Causa raiz:","Área do incidente","Área da solicitação"]
        self.Substitutos = [" "," ","Script vinculado:","Registrar comentário:","Encerrar chamado:","","Tipo do incidente","Tipo da solicitação"]      
        self.Chamado = {}

    def __Chamado__(self,):
         

    def Captura(self,Relatorio):
        TotalDeChamados = len(re.findall(CamposPadroes[0],Relatorio,re.MULTILINE+re.DOTALL))

               ChamadosFatiados = re.findall(DelimitadorDeChamados,Relatorio,re.MULTILINE+re.DOTALL)
        for Iteracao in range(TotalDeChamados): # pega o númearo de chave
            for Campo in CamposPadroes: # pega as expressões regulares de cada campo 
                ExprReg = re.compile(Campo,re.MULTILINE+re.DOTALL) # compila a expressão regular 
                for _Campo in ExprReg.findall(ChamadosFatiados[Iteracao]): # pega o campo no chamado
                    Chave = Iteracao # define os números das chaves que estão em ordem númerica 
                    Chamado[Chave].append(_Campo)
   
        ChamadosProntos = []
        for Chave in range(TotalDeChamados):
            for Conteudo in Chamado[Chave]:
                ChamadosProntos.append(Conteudo)
    
        return(ChamadosProntos)
