import re, json
class Captura():
    '''
        Captura:
            
            Classe para capturar os campos necessários para auditoria dos chamados. 
            Definido em JSON, há expressões regulares para delimitação do chamado e do campo

            Primeiro captura os chamados como lista e os guarda em ordem númerica em um dicionário, que depois será convertido 
            em uma única lista para tratamento.

            O metódo principal dessa classe é Capture(), que será responsável por toda a exceução
    '''

    def __init__(self):

        with open('../dados/CamposPadroesEDelimitador.json','r') as Arquivo:
            Regexs = json.load(Aquivo)

    def Capture(Relatorio):

        DelimitadorDeChamados = list(self.Regexs['DelimitadorDeChamados']) 
        CamposPadroes = list(self.Regexs['CamposPadroes'])
        TotalDeChamados = len(re.findall(CamposPadroes[0],Relatorio,re.MULTILINE+re.DOTALL))
        Chamado = {}

        for Chave in range(TotalDeChamados):
            Chamado[Chave] = [] # Cria lista para cada Chamados

        ChamadosFatiados = re.findall(DelimitadorDeChamados,Relatorio,re.MULTILINE+re.DOTALL)
        for Iteracao in range(TotalDeChamados): # Pega o número de chave
            for Campo in CamposPadroes: # Pega as expressões regulares de cada campo 
                ExprReg = re.compile(Campo,re.MULTILINE+re.DOTALL) # Compila a expressão regular 
                for _Campo in ExprReg.findall(ChamadosFatiados[Iteracao]): # Pega o campo no chamado
                    Chave = Iteracao # Define os números das chaves que estão em ordem númerica 
                    Chamado[Chave].append(_Campo)

        ChamadosProntos = []
        for Chave in range(TotalDeChamados):
            for Conteudo in Chamado[Chave]:
                ChamadosProntos.append(Conteudo)

        return(ChamadosProntos)
   
