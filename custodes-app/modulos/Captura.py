import re, json
class Captura():
    ''' Captura os chamados, os organiza e extraí os campos necessários para auditoria '''
    def __init__(self):
        ''' '''
        self.Responsavel = '__RESPONSAVEL__'
        self.CamposPadroes = ["(?=Solicitação:|Incidente:).+?(?=Em)", "(?=Status:).+?(?=Ativo:)", "(?=Usuário afetado:).+?(?=,)", "(?=Responsável:).+?(?=,)",
                              "(?=Grupo atribuído:).+?(?=Nível)","(?=Área do incidente:|Área da solicitação:).+?(?=\r\n)", "(?=Item de configuração:).+?(?=ChargeBack)",
                              "(?=Descrição:).+?(?=Interrupção|Histórico)",
                              "(?=Script vinculado).+?(?= am| pm|"+self.Responsavel+", )",
                              "(?=Encerrar).+?(?=Pai:|System_AHD_generated)", "Registrar comentário(?!.*Registrar comentário).+?(?="+self.Responsavel+")"]
        self.DelimitadorDeChamados = "(?=Solicitação:|Incidente:).+?(?=Tipo de serviço:)"

    ''' Cria uma lista para cada chave (que estão em ordem númerica) no dicionário 'Chamado' '''
    def __Chamado__(self,TotalDeChamados):
        Chamados = {chave:[] for chave in range(TotalDeChamados)}
        return(Chamados)

    ''' Separe os chamados do relatório e os devolve fatiados (em forma de lista) '''
    def __FatiaOsChamados__(self,Relatorio):
        ChamadosFatiados = re.findall(self.DelimitadorDeChamados,Relatorio,re.MULTILINE+re.DOTALL)
        return(ChamadosFatiados)

    def Captura(self,Relatorio):
        ''' Pega o total de chamados para criar chaves no dicionário 'Chamados' '''
        TotalDeChamados = len(re.findall(self.CamposPadroes[0],Relatorio,re.MULTILINE+re.DOTALL))
        ''' Retorna o dicionário criado para na váriavel 'Chamado' '''
        Chamado = self.__Chamado__(TotalDeChamados)
        ''' Pega os chamados já fatiados '''
        ChamadosFatiados = self.__FatiaOsChamados__(Relatorio)

        ''' Pega o número do chamado que será representado por números (esses números serão 
            a ordem dos chamados capturados)''' 
        for Chave in range(TotalDeChamados):
            ''' Pega o padrão de dada expressão regular para extrair o campo necessário '''
            ''' Variável (ControleDoFor) para controle do loop 'for' '''
            ControleDoFor = 0
            for Campo in self.CamposPadroes:
                ''' Compila a expresão regular da váriavel 'Campo' '''
                ExprReg = re.compile(Campo,re.MULTILINE+re.DOTALL)
                ''' Retorna o campo extraído '''
                for _Campo in ExprReg.findall(ChamadosFatiados[Chave]):
                    Chamado[Chave].append(_Campo)
                ''' Quando o nome do responsável pelo chamado for captura, armazene-o na váriavel 'Responsavel' '''    
                if ControleDoFor == 3:
                    ''' Pega somente o nome do responsável '''
                    self.Responsavel = _Campo.split(':')[1]
                    self.Responsavel = self.Responsavel.replace('\t',"")
                    self.CamposPadroes[8] = self.CamposPadroes[8].replace("__RESPONSAVEL__",self.Responsavel)
                    self.CamposPadroes[10] = self.CamposPadroes[10].replace("__RESPONSAVEL__",self.Responsavel)
                ControleDoFor += 1
            
        ChamadosProntos = []
        for Chave in range(TotalDeChamados):
            for Conteudo in Chamado[Chave]:
                ChamadosProntos.append(Conteudo)
    
        return(ChamadosProntos)
