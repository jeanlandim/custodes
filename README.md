# Custodes
Software para auditoria (interna) de chamados gerados no CA Service Desk Manager. Versão 1.1beta

# O quê é Custodes?
Com o nome baseado no [poema](https://pt.wikipedia.org/wiki/Quis_custodiet_ipsos_custodes%3F) de Juvenal (poeta e retórico romano, autor das Sátiras), Custodes é um software para auditoria (usando tratamento de texto) interna de chamados para equipes de helpdesk usando CA Service Desk Manager.

Filtrando os seguintes campos:
* Tipo (de incidente ou solicitação) 
* Descrição
* Item de configuração
* Soluções (usando scripts ou soluções digitadas pelo o analista)
* Encerrar chamado

Após a filtragem de tais campos, é realizada a verificação de sua conformidade de acordo com regras inseridas pela gestão e supervisão.
O software em si não garante 100% de auditoria, mas permite flexibilidade na hora de auditar chamados.

Abaixo, o exemplo típico de um chamado com tais itens e como são interligados:

![custodes_venn.png](https://github.com/jeanlandim/custodes/raw/master/imgs/custodes_venn.png)

# Changelog

* Versão Alpha descartada
* Nova versão (Versão 1.1beta):

  Será realizada somente a auditoria do sistema, sem necessidade a necessidade de filtrar os dados do relatório cru.
  Um arquivo .csv, será fornecido para cada técnico de Nivel II, contendo os campos dos chamados.

  Os campos que mais interessam para auditoria, são os campos imutáveis. Esses campos são escolhidos pelo responsável (técnico) de acordo com a natureza do chamado.
  - Campos imutáveis: Tipo do chamado, Item de configuração, Soluções baseadas em scripts existentes

  O recurso principal da aplicação será o algoritmo de conformidade de acordo com as regras inseridas pela supervisão.

  
   
# TODO
Refatorar o código para uma semântica mais acessível e profissional do código nas fases beta e estável do programa, e implementar melhorias e recursos de acordo com as exigências da equipe, gestão e supervisão.

# Licença
<b>GPLV3</b>

Custodes - (2019) Jean Landim

Este programa é um software livre; você pode redistribuí-lo e/ou
modificá-lo sob os termos da Licença Pública Geral GNU como publicada
pela Free Software Foundation; na versão 3 da Licença, ou
(a seu critério) qualquer versão posterior.

Este programa é distribuído na esperança de que possa ser útil,
mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
Licença Pública Geral GNU para mais detalhes.

Você deve ter recebido uma cópia da Licença Pública Geral GNU junto
com este programa. Se não, veja <http://www.gnu.org/licenses/>.


