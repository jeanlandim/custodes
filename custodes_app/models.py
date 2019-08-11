from django.db import models
class CustodesAppModels(models.Models):
    def __init__(self):
        # Todos os campos de tipo de solicitação
        TIPOS_DE_SOLICITACAO = [ "(Re)organizar sala técnica", "Abrir/Fechar cadeado", "Acompanhar realização de evento", 
                "Acompanhar visita técnica", "Empréstimo de equipamentos", "Encaminhar para supervisor de 2º nível", 
                "Encaminhar para supervisor de 3º nível", "Formatar micro - apagar dados", "Fornecer informações sobre soluções de TI", 
                "Garantir padrões/segurança (nome, kit seg., software instalado,etc)", "Gerar backup e/ou baixar imagem",
                "Hardware - (des) instalar, (des) ligar, alterar", "Movimentar Equipamento(s)", "Ponto de rede-testar, ativar, desativar, transferir e/ou modificar",
                "Realizar laudo técnico/levantamento", "Realizar manutenção preventiva em equipamento/solução", "Realizar procedimento solicitado pela Infra", 
                "Registrar e acompanhar atendimento de chamado de assistência técnica (4º nível)", "Software - (des) instalar, configurar", 
                "Suporte técnico para realizar evento", "Suporte técnico para realizar videochamada", "Suporte técnico para realizar videoconferência" ]
        # Todos os campos de tipo de incidente
        TIPOS_DE_INCIDENTES = [ "Encaminhar para supervisor de 2º nível", "Encaminhar para supervisor de 3º nível","Erro/falha em conexão de rede",
                "Erro/falha em solução/software","Falta de Suprimentos","Hardware (defeituosos,desconectado, ..)", "Suspeita de vírus/falha segurança" ] 
        # Todos os grupos de atendente 
        GRUPOS = ["Atendente de Suporte Local - DF"]
        # Retorna os tipos de incidente ou solicitação, em uma tupla com as IDs já definidas 
        def __Tipos__(self,tipos):
             tamanho = tipos.length()
             todos_os_tipos = list()
             for tipo in tipos:
                 for id_ in tamanho:
                     todos_os_tipos.append((id_,"Suporte Local."+tipo))
             return todos_os_tipos
         
        SOLICITACAO = __Tipos__(TIPOS_DE_SOLICITACAO)
        INCIDENTES = __Tipos__(TIPOS_DE_INCIDENTES)

# Classe para inserir os scripts no banco de dados.
# Os scripts são imutáveis, porém podem ser modificados e excluídos quando o cliente ou base de documentação achar necessário, mas isso é realizado com pouca frequência
class Scripts(models.Models):
    titulo = models.CharField(max_length=120)
    id_do_script = models.IntegerField()
    descricao_do_script = models.TextField()
    self.SOLICITACAO

# As regras serão baseadas de acordo com o script que foi utilizado na solução de dado chamado, por isso é importante que o script
# contenha informações 
   

# Create your models here.
