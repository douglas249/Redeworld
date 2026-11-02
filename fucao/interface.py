from rich import print
from rich.panel import Panel
from tabulate import tabulate


def cabecalho():
    """ESSA FUNÇÃO É RESPONSAVEL POR MOSTRAR O CABEÇALHO DO PROGRAMA"""

    print('SEJA BEM VINDO AO [green]REDEWORLD[/]!:globe_showing_americas:')


def opcoes_escolha(texto):

    """ESSA FUNÇÃO É RESPONSAVEL POR MOSTRAR AS OPÇÕES DE ESCOLHA DO USUÁRIO"""

    area_trabalho = Panel(
        texto,
        title='[blue]Escolha uma das opções abaixo[/]',
        subtitle='[green]Digite o número da opção desejada[/]'
    )
    print(area_trabalho)


def painel_de_equipamento(roteador, swith, acesspoint):

    """ESSA FUNÇÃO É RESPONSAVEL POR MOSTRAR OS PAINEIS DE EQUIPAMENTOS DISPONIVEIS, 
    UTILIZANDO A BIBLIOTECA TABULATE PARA FORMATAÇÃO DE TABELAS E A BIBLIOTECA RICH PARA ESTILIZAÇÃO, AQUI CADA TABELA RECEBE UM DICIONARIO DO SISTEMA PRINCIPAL"""

    painel = tabulate(roteador,
                   headers= ["EQUIPAMENTO: ROTEADOR", "VALOR DO EQUIPAMENTO"],
                   tablefmt = "grid"
                   )
    mostrar_painel = Panel(painel, title= "EQUIPAMENTO", style = "white", border_style = "green")


    painel1 = tabulate(swith,
                       headers= ["EQUIPAMENTO: SWITH", "VALOR DO EQUIPAMENTO"],
                       tablefmt = "grid"
                       )
    mostrar_painel1 = Panel(painel1, title= "EQUIPAMENTO", style = "white", border_style = "green")

    painel2 = tabulate(acesspoint,
                       headers= ["EQUIPAMENTO: ROTEADOR", "VALOR DO EQUIPAMENTO"],
                       tablefmt = "grid"
                       )
   
    mostrar_painel2 = Panel(painel2, title= "EQUIPAMENTO", style = "white", border_style = "green")
    
  

    print(mostrar_painel, mostrar_painel1, mostrar_painel2)