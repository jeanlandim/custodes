'''
    Importa as bibliotecas de Expressões regulares (re) e JSON (json).
    Importa também classe de formulário do Django
'''
import re, json
from django import forms

class PegaRelatorio(forms.Form):
    '''
            PegaRelatorio:
    
            Pega o relatório inserido na página inicial da aplicação
    '''
    
    relatorio = forms.CharField(
                  widget = forms.Textarea(
                  attrs = {'placeholder': 'Cole aqui o relatório gerado pela CA'}),label='')
    
class CustodesApp():
    # abre os arquivos JSON para extração de campos do relatório e tratamento 
    def __init__(self):
         self.Regexs = {"CamposPadroes":[ "(?=Solicitação:|Incidente:).+?(?=Em)", "(?=Status:).+?(?=Ativo:)", "(?=Usuário afetado:).+?(?=,)", "(?=Responsável:).+?(?=,)", "(?=Grupo atribuído:).+?(?=Nível)",
                        "(?=Área do incidente:|Área da solicitação:).+?(?=Item)", "(?=Item de configuração:).+?(?=ChargeBack)", "(?=Descrição:).+?(?=Interrupção|Histórico)", "Script(?!.*Script).+?(?=Registrar comentário|Encerrar chamado)",
                        "(?=Encerrar).+?(?=Pai:)", "Registrar comentário(?!.*Registrar comentário).+?(?=, fechado)"],
                        "DelimitadorDeChamados":"(?=Solicitação:|Incidente:).+?(?=Tipo de serviço:)"}
         self.Substituicoes = { "CaracteresIndesejados": ["[","]","\'"],
                               "CamposNegritos":["Usuário afetado","Responsável","Área da solicitação", "Item de configuração","Descrição","Status","Grupo atribuído", "Área do incidente","Script vinculado","Encerrar chamado", "Registrar Comentário"], 
                               "Substituir":["\t","\r\n","Script vinculado","Registrar comentário","Encerrar chamado","Causa raiz:","Área do incidente","Área da solicitação"],
                               "Substitutos":[" "," ","Script vinculado:","Registrar comentário:","Encerrar chamado:","","Tipo do incidente","Tipo da solicitação"] }     
         self.Urls = "http://contas.tcu.gov.br/CAisd/pdmweb.exe?OP=SEARCH+FACTORY=cr+SKIPLIST=1+QBE.EQ.ref_num="
     
    def Captura(self,Relatorio):
        '''
            Captura:
                
                Classe para capturar os campos necessários para auditoria dos chamados. 
                Definido em JSON, há expressões regulares para delimitação do chamado e do campo
    
                Primeiro captura os chamados como lista e os guarda em ordem númerica em um dicionário, que depois será convertido 
                em uma única lista para tratamento.
    
                O metódo principal dessa defe é Capture(), que será responsável por toda a exceução
        '''

        DelimitadorDeChamados = self.Regexs['DelimitadorDeChamados']
        CamposPadroes = self.Regexs['CamposPadroes']
        TotalDeChamados = len(re.findall(CamposPadroes[0],Relatorio,re.MULTILINE+re.DOTALL))
        Chamado = {}
    
        for Chave in range(TotalDeChamados):
            Chamado[Chave] = [] # cria lista para cada Chamados
    
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
       
    def Formatar(self,RelatorioCru):
        '''
            Formatar:
    
            Formata o chamado que já foi capturado e extraido. No momento há dois tipos de formatos que serão utilizados: HTML e JSON.
        '''
    
        UrlDoServiceDesk = self.Urls
    
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
                else: # gera o arquivo JSON
                    # numero do chamado será a chave para informações de determinado chamado
                    if Dados.split(":")[0] == "Incidente" or Dados.split(":")[0] == "Solicitação": # pega o número do chamado para usar como chave no arquivo JSON 
                       NumeroDoChamado = Dados.split(":")[1]
                       NumeroDoChamado = NumeroDoChamado.replace(" ","")
                       NovosDadosEmJSON[NumeroDoChamado] = {}
                    elif Dados.split(":")[0] == "Usuário afetado":
                        UsuarioAfetado =  Dados.split(":")[1]
                        NovosDadosEmJSON[NumeroDoChamado]['UsuarioAfetado'] = UsuarioAfetado
                    elif Dados.split(":")[0] == "Responsável":
                        Responsavel = Dados.split(":")[1]
                        NovosDadosEmJSON[NumeroDoChamado]['Responsavel'] = Responsavel
                    elif Dados.split(":")[0] == "Tipo da solicitação" or Dados.split(":")[0] == "Tipo do incidente":
                        _Tipo = Dados.split(":")[1]
                        NovosDadosEmJSON[NumeroDoChamado]['Tipo'] = _Tipo
                    elif Dados.split(":")[0] == "Item de configuração":
                        IC = Dados.split(":")[1]
                        NovosDadosEmJSON[NumeroDoChamado]['IC'] = IC
                    elif Dados.split(":")[0] == "Descrição":
                        Descricao = Dados.split(":")[1]
                        NovosDadosEmJSON[NumeroDoChamado]['Descricao'] = Descricao
                    elif Dados.split(":")[0] == "Status":
                        Status = Dados.split(":")[1]
                        NovosDadosEmJSON[NumeroDoChamado]['Status'] = Status
                    elif Dados.split(":")[0] == "Grupo atribuído":
                        GrupoAtribuido = Dados.split(":")[1]
                        NovosDadosEmJSON[NumeroDoChamado]['GrupoAtribuido'] = GrupoAtribuido
                    elif Dados.split(":")[0] == "Script vinculado":
                        Script = Dados.split(":")[1]
                        NovosDadosEmJSON[NumeroDoChamado]['Script'] = Script
                    elif Dados.split(":")[0] == "Registrar comentário":
                        RegistrarComentario = Dados.split(":")[1]
                        NovosDadosEmJSON[NumeroDoChamado]['RegistrarComentario'] = RegistrarComentario
                    elif Dados.split(":")[0] == "Encerrar chamado":
                        EncerrarChamado = Dados.split(":")[1]
                        NovosDadosEmJSON[NumeroDoChamado]['EncerrarChamado'] = EncerrarChamado
                    return(NovosDadosEmJSON)
            
        return(Formatacao("HTML"))

