import re, json
class Captura():
    ''' Captura os chamados, os organiza e extraí os campos necessários para auditoria '''
    def __init__(self):
        self.CamposPadroes = ["(?=Solicitação:|Incidente:).+?(?=Em)", "(?=Status:).+?(?=Ativo:)", "(?=Usuário afetado:).+?(?=,)", "(?=Responsável:).+?(?=,)",
                              "(?=Grupo atribuído:).+?(?=Nível)","(?=Área do incidente:|Área da solicitação:).+?(?=\r\n)", "(?=Item de configuração:).+?(?=ChargeBack)",
                              "(?=Descrição:).+?(?=Interrupção|Histórico)",
                              "Script(?!.*Script).+?(?=Registrar comentário|Encerrar chamado)",
                              "(?=Encerrar).+?(?=Pai:|System_AHD_generated)", "Registrar comentário(?!.*Registrar comentário).+?(?=, fechado)"]
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
            for Campo in self.CamposPadroes:
                ''' Compila a expresão regular da váriavel 'Campo' '''
                ExprReg = re.compile(Campo,re.MULTILINE+re.DOTALL)
                ''' Retorna o campo extraído '''
                for _Campo in ExprReg.findall(ChamadosFatiados[Chave]):
                    Chamado[Chave].append(_Campo)
            ''' Nem todo chamado tem o campo de script vinculado, e muitas das vezes quando há, é o script de abertura
            '''
            if len(Chamado[Chave])<10:
               Chamado[Chave].append("Não foi encontrado scripts neste chamado. É provável que a solução foi digitada. Para melhor verificação, acesso chamado")
            
            
        ChamadosProntos = []
        for Chave in range(TotalDeChamados):
            for Conteudo in Chamado[Chave]:
                ChamadosProntos.append(Conteudo)
    
        return(ChamadosProntos)
