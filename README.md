
# PROJETO CANCELADO!


# Custodes
Software para auditoria (interna) de chamados gerados no CA Service Desk Manager. Versão 1.0a(lpha)

# O quê é Custodes?
Com o nome baseado no [poema](https://pt.wikipedia.org/wiki/Quis_custodiet_ipsos_custodes%3F) de Juvenal (poeta e retórico romano, autor das Sátiras), Custodes é um software para auditoria (usando tratamento de texto) interna de chamados para equipes de helpdesk usando CA Service Desk Manager.

Filtrando os seguintes itens:
* Tipo (de incidente ou solicitação) 
* Descrição
* Item de configuração
* Soluções (usando scripts ou soluções digitadas pelo o analista)
* Encerrar chamado

Após a filtragem de tais itens, é realizada a verificação de sua conformidade de acordo com regras inseridas pela gestão e supervisão.
O software em si não garante 100% de auditoria, mas permite flexibilidade na hora de auditar chamados.

Abaixo, o exemplo típico de um chamado com tais itens e como são interligados:

![custodes_venn.png](https://github.com/jeanlandim/custodes/raw/master/imgs/custodes_venn.png)

# Changelog

## 01/08/2019
* Realizada a manutenção nos cards do chamado para chamados "Não resolvido, fechado" não incluir os demais chamados dentro
do seu card.

## 21/07/2018:
* Refeita a template final de formatação dos chamados utilizando o content container de cards
* Retirado o JSON para suporte a auditoria
* Versão Alpha atingida (1.0a)

## 30/06/2019:
* Abrir chamados em uma nova aba.
* Adicionado o JSON para suporte a auditoria
* Refatorado o código

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


