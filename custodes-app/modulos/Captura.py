import re, json
class Captura():
    ''' Captura os chamados, os organiza e extraí os campos necessários para auditoria '''
    def __init__(self):
        self.CamposPadroes = ["(?=Solicitação:|Incidente:).+?(?=Em)", "(?=Status:).+?(?=Ativo:)", "(?=Usuário afetado:).+?(?=,)", "(?=Responsável:).+?(?=,)",
                              "(?=Grupo atribuído:).+?(?=Nível)","(?=Área do incidente:|Área da solicitação:).+?(?=Item)", "(?=Item de configuração:).+?(?=ChargeBack)",
                              "(?=Descrição:).+?(?=Interrupção|Histórico)",
                              "Script(?!.*Script).+?(?=Registrar comentário|Encerrar chamado)",
                              "(?=Encerrar).+?(?=Pai:)", "Registrar comentário(?!.*Registrar comentário).+?(?=, fechado)"]
        self.DelimitadorDeChamados = "(?=Solicitação:|Incidente:).+?(?=Tipo de serviço:)"

    ''' Cria uma lista para cada chave (que estão em ordem númerica) no dicionário 'Chamado' '''
    def __Chamado__(self,TotalDeChamados):
        Chamados = {chave:[] for chave in range(TotalDeChamados)}
        return(Chamados)

    ''' Separe os chamados do relatório e os devolve fatiados (em forma de lista) '''
    def __FatiaOsChamados__(self,Relatorio):
        ChamadosFatiados = re.findall(DelimitadorDeChamados,Relatorio,re.MULTILINE+re.DOTALL)
        return(ChamadosFatiados)

    def Captura(self,Relatorio):
        ''' Pega o total de chamados para criar chaves no dicionário 'Chamados' '''
        TotalDeChamados = len(re.findall(CamposPadroes[0],Relatorio,re.MULTILINE+re.DOTALL))
        
        for Chave in range(TotalDeChamados): ''' Pega o número do chamado ''' 
            for Campo in CamposPadroes: ''' Pega o padrão de dada expressão regular para extrair o campo necessário ''' 
                ExprReg = re.compile(Campo,re.MULTILINE+re.DOTALL) ''' Conpila a expresão regular da váriavel 'Campo' '''
                for _Campo in ExprReg.findall(ChamadosFatiados[Chave]): ''' Retorna o campo extraído '''
                    Chamado[Chave].append(_Campo)
   
        ChamadosProntos = []
        for Chave in range(TotalDeChamados):
            for Conteudo in Chamado[Chave]:
                ChamadosProntos.append(Conteudo)
    
        return(ChamadosProntos)
