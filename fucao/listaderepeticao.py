from rich import print
from time import sleep

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

        escolha = str(input(f'Voce deseja usar {equipamento} [green][SIM/NÃO?][/]'))

        quantidade = str(input(f'Qual será a quantidade de {equipamento} usurá?'))

    if escolha == "SIM":
        print(f'O equipamento [green]{equipamento}[/] foi selecionado!')
        print(f'A quantidade de {equipamento} é {quantidade}')
    else:
        print(f'[red]Equipamento[/] {equipamento} [red]não selecionado.[/]')

    escolhidos = {}

    escolhidos[equipamento] = quantidade

    for equipamento, quantidade in escolhidos:
        resultado = quantidade * 2
        reserva = resultado + (resultado * 10 / 100)
    print(f'O seu equipamento é {equipamento}e voce vai precisar {resultado} de conectores para o seu projeto')
    print(f'[RED]IMPORTANTE[/] Separe {reserva} quantidade de conectores para reserva!')

    print('Calcular área do projeto')
    print('[red]Carregando...[/]')
    sleep(1)

    for espaco in quantidade:
        area = int(input('Qual é a quantidade de metros quadrados do seu projeto?'))
        distancia = int(input('Qual vai ser a distancia entre os equipamentos?'))
        total = distancia * espaco
        espaco_total = area + total

        print(f'A área total do seu projeto é {espaco_total}')

    print('Calcular quantidade de caixas de conectores')
    print('[red]Carregando...[/]')
    sleep(1)

    metros = espaco_total
    caixas = metros / 305

    print(f'Seu projeto precisará de {espaco_total} metros de cabo de rede e {caixas} caixas de cabo de rede.')

           

        

    
