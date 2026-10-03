from rich import print
from rich.panel import Panel


def cabecalho():
    print('SEJA BEM VINDO AO [green]REDEWORLD[/]!:globe_showing_americas:')




def opcoes_escolha(texto):
    area_trabalho = Panel(texto, title='[blue]Escolha uma das opções abaixo[/]', subtitle='[green]Digite o número da opção desejada[/]')
    print(area_trabalho)
    



def painel_de_equipamento(roteador, switch, acesspoint):
    mostrar = Panel(f"Roteador: {roteador}\nSwitch: {switch}\nAccess Point: {acesspoint}", title='[blue]Equipamentos disponíveis[/]', subtitle='[green]Escolha o equipamento desejado[/]')
    print(mostrar)


