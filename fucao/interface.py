from rich import print
from rich.panel import Panel


def cabecalho():
    print('SEJA BEM VINDO AO [green]REDEWORLD[/]!:globe_showing_americas:')



def opcoes_escolha():
    area_trabalho = Panel('[blue][ 1 ][/] calcular quantidade de conectores e caixas de rede.\n\n'    '[blue][ 2 ][/] ver listagens de preço de equipamentos atual.\n\n'    '[blue][ 3 ][/] Calcular os preços entre os equipamentos.\n\n'     '[blue][ 4 ][/] Salvar e encerrar.', title = "ÁREA DE TRABALHO", width = 45)
    print(area_trabalho)

gg = opcoes_escolha()
print(gg)

