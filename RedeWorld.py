# ADICIONEI ALGUMAS BIBLIOTECAS PARA MELHORAR O PROGRAMA#      
from rich import print
from time import sleep

from fucao import interface
from fucao import listaderepeticao
from fucao import funcionalidades




#LISTA DE EQUIPAMENTOS PARA CALCULOR DE VALOR NA OPÇÃO 3#
roteadorescisco = {
      
   #ROTEADORES CISCO
   "ISR_1100": 2500,
   "ISR_4321": 5600,
   "ISR_4331": 7000,
   "ISR_4431": 15000,
}


switchscisco = {
      
   #SWITCHS CISCO
   "Catalyst_C1200_24T_4G": 2790,
   "Catalyst_C1200_24P_4G": 4000,
   "Catalyst_C1200_48P_4G": 59309,}


acesspointscisco = {
      
   #ACEESS POINTS CISCO
   "Meraki_MR33": 1.0,
   "Meraki_MR36": 3.7,
   "Meraki_MR46": 3.0,
   "Meraki_CW9164": 11.0,
   "Meraki_CW9166": 15.8, 

   }

roteadoreTPLINK = {
      
   #ROTEADORES TP LINK
   "TLWR840N": 114,
   "Archer_C50": 210,
   "Archer_AX53": 260,
   "Archer_BE550": 1.3,
}

switchTPLINK = {
      
   #SWITCHS TP LINK
   "TLSG105": 110,
   "TLSG108": 150,
   "TLSG1016D": 553,
   "TLSG1024D": 900,
   "TLSG1008MP": 770,
   "T2600G28TS": 1.359,
   
   }

acesspointTPLINK = {
      
   #ACESS POINTS TP LINK
   "EAP115": 220,
   "EAP225": 505,
   "EAP610": 720,
   "EAP613": 369,
   "EAP650": 998,
}

roteadoresINTELBRAS = {
      
   #ROTEADORES INTELBRAS
   "W4_300S": 160,
   "W5_1200G": 220,
   "W5_1200GS": 250,
   "W6_1500": 328,
   "RX_3000": 473,
}

switchINTELBRAS = {
      
    #SWITCHS INTELBRAS
   "SF800Q": 80,
   "S1116G": 660,
   "S1124G": 830,
   "S1110G_PA": 875,
   "S1120G_PA": 1.903,
   "S1128G_PA": 2.633,
}

acesspointINTELBRAS = {
      
    #ACESS POINTS INTELBRAS
   "AP_3_10": 320,
   "AP_3_60": 702,
   "AP_12_10_AC": 529,
   "AP1250ACMax": 1.006,
   "AP1250ACOutdoor": 1.120,
   "AP_13_50_AC_S": 890,
}

lista_total_equipamentos = [acesspointINTELBRAS, switchINTELBRAS, roteadoresINTELBRAS,   
                           acesspointTPLINK, switchTPLINK, roteadoreTPLINK, 
                           acesspointscisco, switchscisco, roteadorescisco   ]

#TODOS EQUIPAMENTOS E PREÇOS#

# CHAMANDO A FUNÇÃO DE APRESENTAÇÃO
interface.cabecalho()
sleep(1)

opção = 0

# UMA ESTRUTURA DE REPETIÇAO, REPETE AS OPÇÃO
while opção != 4:
#DENTRO DO WHILE ADICIONEI ALGUMAS OPÇÕES PARA QUE O USUARIO ESCOLHA OQUE FAZER E DE COMO USAR O PROGRAMA#
   interface.opcoes_escolha('[blue][ 1 ][/] calcular quantidade de conectores e caixas de rede.\n\n'
    '[blue][ 2 ][/] ver listagens de preço de equipamentos atual.\n\n'   '[blue][ 3 ][/] Calcular os preços entre os equipamentos.\n\n'  '[blue][ 4 ][/] Salvar e encerrar.')

   opcao = int(input('Qual opção deseja?'))

#NA OPÇÃO 1 ADICIONEI O CALCULO DE CAIXAS DE REDE E CONECTORES#
   if opcao == 1:

      print('Opção 1 selcionada, [green]vamos calcular[/]!...')
      sleep (1)

      listaderepeticao.escolhendo_equipamento()

   if opção == 2:
#AQUI ADICIONEI MAIS ALGUNS IF (CONDIÇOES ANINHADAS) PARA QUE O USUARIO ESCOLHA MARCA E EQUIPAMENTO#
      interface.opcoes_escolha('[ 1 ] Cisco System\n\n'  '[ 2 ] TP-Link\n\n' '[ 3 ] Intelbras\n\n')
      opção1 = int(input('Escolha uma marca: '))
      if opção1 == 1:
            print ('Opção [green]1[/] selcionada...')
            sleep (1)

            interface.painel_de_equipamento(roteadorescisco, switchscisco, acesspointscisco)
         
      if opção1 == 2:
         print ('Opção [green]2[/] selcionada...')
         sleep (1)

         interface.painel_de_equipamento(roteadoreTPLINK, switchTPLINK, acesspointTPLINK)
         
      if opção1 == 3:
               print ('Opção [green]3[/] selcionada...')
               sleep (1)

               interface.painel_de_equipamento(roteadoresINTELBRAS, switchINTELBRAS, acesspointINTELBRAS)
               
   if opção == 3:
#RESPOTA DA LISTA DE EQUIPAMENTOS:
       funcionalidades.calcular_valor_equipamento(lista_total_equipamentos)
      
         
   if opção == 4:
      sleep(1)
      pass

    

 