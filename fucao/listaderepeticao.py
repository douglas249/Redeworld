from rich import print
from time import sleep
import math


def lista_equipamento():
    """ESSA FUNCAO FICA RESPONSAVEL POR RECEBER OS EQUIPAMENTOS DISPONIVEI 
    PARA O USUARIO PARA ESCOLHER """

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
    
    """ESSA FUNCAO PEGA A LISTA DE EQUIPAMENTOS DA FUNCAO DE LISTA_EQUIPAMENTO
    E FA UMA SELEÇAO DE EQUIPAMENTOS QUE O USUARIO DESEJAR UTILIZAR NO PROJETO, SALVANDO OS QUE ELE DESEJA EM UM DICIONARIO. FICA NA OPÇAO 1 DO SISTEMA PRINCIPAL"""
    
    lista = lista_equipamento() 
    
    for equipamento in lista:
        
            while True:
                try:
                      
                    escolha = str(input(f'Deseja usar o {equipamento} no seu prjeto? [SIM/NÃO]?')).strip()      

                    if escolha != 'SIM' and escolha != 'sim' and escolha != 'NÃO' and escolha != 'não' and escolha != 'nao' and escolha != 'NAO':
                        raise ValueError("Opção inválida. Digite 'SIM' ou 'NÃO'.")
                except ValueError as e:
                    print(e)
                    continue
                else:
                    break
            
                    

            if escolha == 'SIM' or escolha == 'sim': 

                print(f'O equipamento [green]{equipamento}[/] foi selecionado!')
                while True:
                    try:

                     quantidade = int(input(f'Qual será a quantidade de equipamento de {equipamento} usurá para o seu prjeto?'))

                    except ValueError:
                        
                        print('[red]ERRO![/] Digite um número inteiro válido')
                    else:
                        print(f'A quantidade de {equipamento} é {quantidade}')
                        break

                escolhidos = {}
                                                
                escolhidos[equipamento] = quantidade

            else:
                if escolha == 'NÃO' or escolha == 'não' or escolha == 'nao' or escolha == 'NAO':
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
            while True:
                try:

                    area = int(input('Qual é a quantidade de metros quadrados do seu projeto?'))
                    distancia = int(input('Qual vai ser a distancia entre os equipamentos?'))


                except ValueError:
                    
                    print('[red]ERRO![/] Digite um número inteiro válido')

                else:
                    total = distancia * quantidade
                    espaco_total = area + total
                    break


            print(f'A área total do seu projeto é {espaco_total}')


    print('Calcular quantidade de caixas de conectores')
    print('[red]Carregando...[/]')
    sleep(1)

    metros = espaco_total
    caixas = metros / 305

    print(f'Seu projeto precisará de [orange]{espaco_total}[/] metros de cabo de rede e [yellow]{math.ceil(caixas)}[/] caixas de cabo de rede.')
    return escolhidos, quantidade, espaco_total, caixas

           

        

    
