from rich import print
from time import sleep
import math


def lista_equipamento():

    """ESSA FUNÇÃO RECEBE TODOS OS EQUIPAMENTOS E OS GUARDA"""
    equipamento = ["computador",
                    "switch",
                    "switch gerenciavel",
                    "DVR",
                    "roteadores",
                    "servidores de arquivo",
                    "impressoras"]

    return equipamento




def escolhendo_equipamento():
    """ESSA FUNÇÃO PEGA OS EQUIPAMENTOS DA LISTA DA FUNÇÃO LISTA_EQUIPAMENTO E FAZ UMA SELEÇÃO"""
    
    lista = lista_equipamento() 

    for equipamento in lista:

        escolha = str(input(f'Deseja usar o {equipamento} no seu prjeto? [SIM/NÃO]?'))

        if escolha == 'SIM' or escolha == 'sim':
            print(f'O equipamento [green]{equipamento}[/] foi selecionado!')

            quantidade = int(input(f'Qual será a quantidade de equipamento de {equipamento} usurá para o seu prjeto?'))

            print(f'A quantidade de {equipamento} é {quantidade}')

            escolhidos = {}
            
            escolhidos[equipamento] = quantidade

        else:
            print(f'O [red]equipamento {equipamento}[/] não foi selecionado.')


    for equipamento, quantidade in escolhidos.items():
        resultado = quantidade * 2
        reserva = resultado + (resultado * 10 / 100)
        print(f'O seu equipamento é {equipamento} e voce vai precisar {resultado} de conectores para o seu projeto')
        print(f'[red]IMPORTANTE[/] Separe {reserva} quantidade de conectores para reserva!')

    print('Calcular área do projeto')
    print('[red]Carregando...[/]')
    sleep(1)

    for equipamento, quantidade in escolhidos.items():
        area = int(input('Qual é a quantidade de metros quadrados do seu projeto?'))
        distancia = int(input('Qual vai ser a distancia entre os equipamentos?'))
        total = distancia * quantidade
        espaco_total = area + total

        print(f'A área total do seu projeto é {espaco_total}')

    print('Calcular quantidade de caixas de conectores')
    print('[red]Carregando...[/]')
    sleep(1)

    metros = espaco_total
    caixas = metros / 305

    print(f'Seu projeto precisará de [orange]{espaco_total}[/] metros de cabo de rede e [yellow]{math.ceil(caixas)}[/] caixas de cabo de rede.')

           

        

    
