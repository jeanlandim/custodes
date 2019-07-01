import re, json
from django import forms
    
class CustodesApp(forms.Form):
    # abre os arquivos JSON para extração de campos do relatório e tratamento 
    def __init__(self):
        with open('../dados/CamposPadroesEDelimitador.json','r') as Campos:
             Regexs = json.load(Campos)
        with open('../dados/Substitutos.json','r') as Substitutos:
             Substituicoes = json.load(Substitutos)              
        with Open('../dados/Urls.json','r') as Url:
             Urls = json.load(Url)
    
    def PegaRelatorio():
        '''
            PegaRelatorio:
    
            Pega o relatório inserido na página inicial da aplicação
        '''
    
        relatorio = forms.CharField(
                  widget = forms.Textarea(
                  attrs = {'placeholder': 'Cole aqui o relatório gerado pela CA'}),label='')
    
    def Captura(Relatorio):
        '''
            Captura:
                
                Classe para capturar os campos necessários para auditoria dos chamados. 
                Definido em JSON, há expressões regulares para delimitação do chamado e do campo
    
                Primeiro captura os chamados como lista e os guarda em ordem númerica em um dicionário, que depois será convertido 
                em uma única lista para tratamento.
    
                O metódo principal dessa defe é Capture(), que será responsável por toda a exceução
        '''

    
        DelimitadorDeChamados = list(self.Regexs['DelimitadorDeChamados']) 
        CamposPadroes = list(self.Regexs['CamposPadroes'])
        TotalDeChamados = len(re.findall(CamposPadroes[0],Relatorio,re.MULTILINE+re.DOTALL))
        Chamado = {}
    
        for Chave in range(TotalDeChamados):
            Chamado[Chave] = [] # cria lista para cada Chamados
    
        ChamadosFatiados = re.findall(DelimitadorDeChamados,Relatorio,re.MULTILINE+re.DOTALL)
        for Iteracao in range(TotalDeChamados): # pega o número de chave
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
       
    def Formatar(RelatorioCru):
        '''
            Formatar:
    
            Formata o chamado que já foi capturado e extraido. No momento há dois tipos de formatos que serão utilizados: HTML e JSON.
        '''
    
        UrlDoServiceDesk = self.Urls["Urls"]
    
        def PreFormatacao(self,RelatorioCru):
            DadosLimpos = []
            CaracteresIndesejados = self.Substituicoes['CaracteresIndesejados']
            Substituir = self.Substituicoes['Substituir']
            Substitutos = self.Substituicoes['Substituitos']
            
            for TextoCru in RelatorioCru:
                TextoCru = str(TextoCru) 
                for Caracter in CaracteresIndesejados:
                    TextoCru = TextoCru.replace(Caracter,"")
                for Indice in range(len(Substituir)): 
                    TextoCru = TextoCru.replace(Substituir[Indice],Substitutos[Indice])
                DadosLimpos.append(TextoCru)

            return(DadosLimpos)
    
        def Formatacao(self,Tipo):
            DadosLimpos = PreFormatacao(RelatorioCru)
            Tipos = ["HTML","JSON"]
            NovosDadosEmHTML = []
            NovosDadosEmJSON = {}
            CamposEmNegrito = self.Substitucoes['CamposNegritos']

            for Dados in DadosLimpos 
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
                else: # gera o arquivo JSON
                    # numero do chamado será a chave para informações de determinado chamado
                    if Dados.split(":")[0] == "Incidente" or Dados.split(":")[0] == "Solicitação": # pega o número do chamado para usar como chave no arquivo JSON 
                       NumeroDoChamado = Dados.split(":")[1]
                       NumeroDoChamado = NumeroDoChamado.replace(" ","")
                    else if Dados.split(":")[0] == "Usuário afetado":
                        UsuarioAfetado = Dados.split(":")[1]
                    else if Dados.split(":")[0] == "Responsável":
                        Responsavel = Dados.split(":")[1]
                    else if Dados.split(":")[0] == "Tipo da solicitação" or Dados.split(":")[0] == "Tipo do incidente":
                        _Tipo = Dados.split(":")[1]
                    else if Dados.split(":")[0] == "Item de configuração":
                        IC = Dados.split(":")[1]
                    else if Dados.split(":")[0] == "Descrição":
                        Descricao = Dados.split(":")[1]
                    else if Dados.split(":")[0] == "Status":
                        Status = Dados.split(":")[1]
                    else if Dados.split(":")[0] == "Grupo atribuído":
                        GrupoAtribuido = Dados.split(":")[1]
                    else if Dados.split(":")[0] == "Script vinculado":
                        Script = Dados.split(":")[1]
                    else if Dados.split(":")[0] == "Registrar comentário":
                        RegistrarComentario = Dados.split(":")[1]
                    else if Dados.split(":")[0] == "Encerrar chaamdo":
                        EncerrarChamado = Dados.split(":")[1]
                

                    NovosDadosEmJSON[NumeroDoChamado].append({'Chamado':NumeroDoChamado,
                           'UsuarioAfetado':UsuarioAfetado,
                           'Responsavel':Responsavel,
                           'Tipo':_Tipo,
                           'IC':IC,
                           'Descricao':Descricao,
                           'Status':Status,
                           'Grupo':GrupoAtribuido,
                           'Script':Script
                           'RegistrarComentario':RegistrarComentario,
                           'Encerrar':EncerrarChamado})
                    return(NovosDadosEmJSON)

