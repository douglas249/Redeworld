# ADICIONEI ALGUMAS BIBLIOTECAS PARA MELHORAR O PROGRAMA#
import math
from time import sleep
from tabulate import tabulate
#COLOCANDO VARIAVEIS GLOBAIS PARA O CALCULO DE VALORES ENTRE EQUIPAMENTOS NA OPÇÃO 2#
equipamentos = {
   "Catalyst_C1200_24T_4G": 2790,
   "Catalyst_C1200_24P_4G": 4000,
   "Catalyst_C1200_48P_4G": 59309,
   "ISR_1100": 2500,
   "ISR_4321": 5600,
   "ISR_4331": 7000,
   "ISR_4431": 15000,
   "Meraki_MR33": 1.0,
   "Meraki_MR36": 3.7,
   "Meraki_MR46": 3.0,
   "Meraki_CW9164": 11.0,
   "Meraki_CW9166": 15.8,
   "TLWR840N": 114,
   "Archer_C50": 210,
   "Archer_AX53": 260,
   "Archer_BE550": 1.3,
   "TLSG105": 110,
   "TLSG108": 150,
   "TLSG1016D": 553,
   "TLSG1024D": 900,
   "TLSG1008MP": 770,
   "T2600G28TS": 1.359,
   "EAP115": 220,
   "EAP225": 505,
   "EAP610": 720,
   "EAP613": 369,
   "EAP650": 998,
   "W4_300S": 160,
   "W5_1200G": 220,
   "W5_1200GS": 250,
   "W6_1500": 328,
   "R_3000": 473,
   "SF800Q": 80,
   "S1116G": 660,
   "S1124G": 830,
   "S1110G_PA": 875,
   "S1120G_PA": 1.903,
   "S1128G_PA": 2.633,
   "AP_3_10": 320,
   "AP_3_60": 702,
   "AP_12_10_AC": 529,
   "AP1250ACMax": 1.006,
   "AP1250ACOutdoor": 1.120,
   "AP_13_50_AC_S": 890,
}







}

quantidade = int(input("Quantos equipamentos você deseja calcular? "))

total = 0

for i in range(quantidade):
    nome = input(f"Digite o nome do {i+1}º equipamento: ")

    if nome in equipamentos:
        preco = equipamentos[nome]
        print(f"{nome} custa R$ {preco:,.2f}")
        total += preco
    else:
        print("Equipamento não encontrado!")

print(f"\nValor total: R$ {total:,.2f}")


ISR_1100 = 2.500
ISR_4321 = 5.600
ISR_4331 = 7.000
ISR_4431 = 15.000
Catalyst_C1200_24T_4G =2.790
Catalyst_C1200_24T_4G =2.790
Catalyst_C1200_24P_4G =4.000
Catalyst_C1200_48P_4G =9.309
Catalyst_2960_X_2 =42.000
Catalyst_9200L_48T_4G_E =21.241
Catalyst_9200_48P_E =9.949
Meraki_MR33 = 1.000
Meraki_MR36  =3.700
Meraki_MR46 = 3.000  
Meraki_CW9164 = 11.000  
Meraki_CW9166 = 15.800  
TLWR840N = 114
Archer_C50 = 210
Archer_AX53 = 260
Archer_BE550 = 1.300
TLSG105	=	110
TLSG108	=	150
TLSG1016D	=	553
TLSG1024D	=	900
TLSG1008MP	=	770
T2600G28TS	=	1.359
EAP115 =220
EAP225 =505
EAP610 =720
EAP613 =369
EAP650 =998
W4_300S= 160
W5_1200G= 220 
W5_1200GS= 250
W6_1500 =328
R_3000 = 473
SF800Q = 80
S1116G = 660
S1124G = 830
S1110G_PA = 875
S1120G_PA = 1.903
S1128G_PA = 2.633
AP_3_10 = 320
AP_3_60 = 702
AP_12_10_AC = 529
AP1250ACMax = 1.006
AP1250ACOutdoor = 1.120
AP_13_50_AC_S = 890
#TODOS EQUIPAMENTOS E PREÇOS#

#PROGRAMA#
print ('Bem vindo ao RedeaWorld, aqui voce poderá calcular a quantidade de conectores RJ45 e caixas de cabo de rede para o seu prjeto!')
sleep(1)
opção = 0
#ADICIONEI UMA ESTRUTURA PARA QUE O PROGRAMA NÃO SEJA ENCERRADO DE FORMA INDESEJADA#
while opção != 5:
#DENTRO DO WHILE ADICIONEI ALGUMAS OPÇÕES PARA QUE O USUARIO ESCOLHA OQUE FAZER E DE COMO USAR O PROGRAMA#
   print ( '[ 1 ] calcular quantidade de conectores e caixas de rede\n'  '[ 2 ] ver listagens de preço de equipamentos atual\n' '[ 3 ] Calcular os preços entre os equipamentos\n'     '[ 4 ] Salvar e encerrar')
   opção = int(input('Qual opção deseja?'))
#NA OPÇÃO 1 ADICIONEI O CALCULO DE CAIXAS DE REDE E CONECTORES#
#NA OPÇÃO 2 ADICIONEI UMA LISTAGEM DE EQUIPAMENTOS COM SEUS RESPECTIVOS PREÇOS#
#NA OPÇÃO 3 ADICIONEI UM PROGRAMA PARA FAZER UM SALVAMENTO DE TODOS OS DADOS NO EXCEL#
   if opção == 1:

      print ('Opção 1 selcionada, vamos calcular!...')
      sleep (1)

      #pegando informaçoes#

      print ('Tem que ter a requisição de equipamentos, por favor digite abaixo os equipamentos:')
      computadores = switchs = switchsgre = dvrs = impressoras = servidorarq = roteadores = 0

      resposta = str(input('Voce deseja usar computadores [SIM/NÃO]?'))
      if resposta == 'sim':
         computadores = int(input('Quantos computadores usará?'))
      else:
         pass
      resposta1 = str(input('Voce deseja usar switchs [SIM/NÃO]?'))
      if resposta1 == 'sim':
         switchs = int(input('Quantos swithcs usará?'))
      else:
         pass
      resposta2 = str(input('Voce deseja usar switchs gerenciaveis [SIM/NÃO]?'))
      if resposta2 == 'sim':
         switchsgre = int(input('Quantos usará?'))
      else:
         pass
      resposta3 = str(input('Voce deseja usar DVR [SIM/NÃO]?'))   
      if resposta3 == 'sim':
         dvrs = int(input('Quantos DVR usará?'))
      else:
         pass
      resposta4 = str(input('Voce deseja usar impressoras [SIM/NÃO]?'))   
      if resposta4 == 'sim':
         impressoras = int(input('Quantas impressoras usará?'))
      else:
         pass
      resposta5 = str(input('Voce deseja usar servidores de arquivos [SIM/NÃO]?'))
      if resposta5 == 'sim':
         servidorarq = int(input('Quantos usará?'))
      else:
         pass
      resposta6 = str(input('Voce deseja usar roteadores [SIM/NÃO]?'))
      if resposta6 == 'sim':
         roteadores = int(input('Quantos roteadores usará?'))
      else:
         pass
      
      #Fazendo a soma dos componentes para quantidade de conectores RJ45# 

      conectores1 = computadores * 2
      conectores2 = switchs * 2
      conectores3 = switchsgre * 2
      conectores4 = dvrs * 2 
      conectores5 = impressoras * 2
      conectores6 = servidorarq * 2
      conectores7 = roteadores * 2
      #Resposta:#
      print ('A quantidade de computadores é {} e a quantidade de conectores para conexão é {}'.format(computadores,conectores1))

      print ('A quantidade de switchs é {} e a quantidade de conectores para conexão é {}'.format(switchs,conectores2))

      print ('A quantidade de switchs gerenciaveis é {} e a quantidade de conectores para conexão é {}'.format(switchsgre,conectores3))

      print ('A quantidade de switchs gerenciaveis é {} e a quantidade de conectores para conexão é {}'.format(dvrs,conectores4))

      print ('A quantidade de impressoras que serão utilizados é {} e a qauntidade de conectores necessários é {}'.format(impressoras, conectores5))

      print ('A quantidade de servidores que serão utilizados é {} e a quantidade de conectores necessários é {} '.format(servidorarq, conectores6))

      print ('A quantidade de roteadores utilizados é {} e a quantidade de conectores necessários {}'.format(roteadores, conectores7))

      #resposta total:#

      totalconec = conectores1 + conectores2 + conectores3 + conectores4 + conectores5 + conectores6 + conectores7
      reservaconec = totalconec + (totalconec * 10 / 100)
      print (f'Total de conectores que serão utilizados: {totalconec} CONECTORES')

      print ('IMPORTANTE! mantenha sempre uma pequena quantidade de conectores como reserva para eventuais contra tempos. no seu caso recomendo {} conectores'.format(math.ceil(reservaconec)))
      #Calculando o tamanho da area e distancia dos equipamentos#
      area = int(input('Qual é a quantidade de metros quadrados do seu projeto?'))

      distancia = int(input('Qual vai ser a distancia entre os equipamentos?'))
      total = distancia * computadores * switchs * switchsgre * dvrs * impressoras * servidorarq * roteadores
      total1 = total + area

      #Dando resposta de acordo com o tamanho da distancie entre os computadores#

      if distancia >= 5 and distancia <= 10:
         print ('A area total dos computadores é {}'.format(total1))
      elif distancia >= 11 and distancia <= 20:
         print ('A area total dos computadores é {}'.format(total1))
      elif distancia >= 21 and distancia <= 30:
         print ('A area total dos computadores é {}'.format(total1))
      elif distancia >= 31 and distancia <= 40:
         print ('A area total dos computadores é {}'.format(total1))             
      elif distancia >= 41 and distancia <= 50:
         print ('A area total dos computadores é {}'.format(total1))
      elif distancia >= 51 and distancia <= 60:
         print ('A area total dos computadores é {}'.format(total1))
      elif distancia >= 61 and distancia <= 70:
         print ('A area total dos computadores é {}'.format(total1))             
      elif distancia >= 71 and distancia <= 80:
         print ('A area total dos computadores é {}'.format(total1))
      elif distancia >= 81 and distancia <= 90:
         print ('A area total dos computadores é {}'.format(total1))
      elif distancia >= 91 and distancia <= 100:
         print ('A area total dos computadores é {}'.format(total1))   
         
      #Fazendo o calculo de quantas caixas de cabo de rede serão necessárias para o projeto#

      metros = total1
      caixas = metros / 305
      #resposta#
      print ('A área total do seu projeto é de {}m² e irá precisar de {} caixas de cabo de rede'.format(total1,math.ceil(caixas)))
   if opção == 2:
#AQUI ADICIONEI MAIS ALGUNS IF (CONDIÇOES ANINHADAS) PARA QUE O USUARIO ESCOLHA MARCA E EQUIPAMENTO#
      print ('Qual marca de equipamento?')
      print ('[ 1 ] Cisco System\n'  '[ 2 ] TP-Link\n' '[ 3 ] Intelbras\n')
      opção1 = int(input('Escolha uma marca: '))
      if opção1 == 1:
         equipamento = str(input('Ver roteadores, switchs ou access Point?'))
         sleep(1)
         #MOSTRANDO EQUIPAMENTOS#
         if equipamento == 'roteadores':
            print ('ROTEADORES CISCO')
            #VARIAVEIS PARA CALCULOS#
            ISR_1100 = 2.500
            ISR_4321 = 5.600
            ISR_4331 = 7.000
            ISR_4431 = 15.000
            roteadorestotaiscisco = ISR_1100 + ISR_4321 + ISR_4331 + ISR_4431
            #RESPOSTA#
            lista = [
               [" ISR_1100 Series", "Pequenas empresas", "1.300 – 2.500$"],
               [" ISR_4321", "Filiais e escritórios", "2.700 – 5.600$"],
               [" ISR_4331", "Médio porte", "1.700 – 7.000$"],
               [" ISR_4431", "Grande porte", "7.900 – 15.000"],
            ]
            print(tabulate(
               lista,
               headers=["Modelo Cisco", "Descrição", "Preço médio (R$)"],
               tablefmt="grid"
            ))
            #A ESTRUTURA ADIANTE SEGUE DA MESMA FORMA E PADRÃO DE COMANDOS#
            print ('----------------------------------------------------------------------------------------------')
         elif equipamento == 'switchs':
            print ('SWITCHS CISCO')
            Catalyst_C1200_24T_4G =2.790
            Catalyst_C1200_24P_4G =4.000
            Catalyst_C1200_48P_4G =9.309
            Catalyst_2960_X_2 =42.000
            Catalyst_9200L_48T_4G_E =21.241
            Catalyst_9200_48P_E =9.949
            totaisswitchscisco = Catalyst_C1200_24T_4G + Catalyst_C1200_24P_4G + Catalyst_C1200_48P_4G + Catalyst_2960_X_2 + Catalyst_9200L_48T_4G_E + Catalyst_9200_48P_E
            lista1 = [   
                           ["Catalyst_C1200_24T_4G", "Switch Gigabit 24 portas", "2.790$"],
                           ["Catalyst_C1200_24P_4G", "Switch Gigabit 24 portas PoE", "4.000$"],
                           ["Catalyst_C1200_48P_4G", "Switch Gigabit 48 portas PoE", "9.309$"],
                           ["Catalyst_2960_X_24", "Switch corporativo 24 portas", "2.000$"],
                           ["Catalyst_9200L_48T_4G_E", "Switch Layer 3 empresarial", "21.241$"],
                           ["Catalyst_9200-48P_E", "Switch Layer 3 PoE 48 portas", "9.949$"]
                           
                           ]

            
            print(tabulate(
                     lista1,
                     headers=["Modelo Cisco", "Descrição", "Preço médio (R$)"],
                     tablefmt="grid"     
                  ))

            equipamentototais = str(input('Deseja escolher um equipamento para calcular o preço total [SIM/NÃO]?'))
            if equipamentototais == 'SIM' or equipamentototais == 'sim':
                 
          
             print('----------------------------------------------------------------------------------------------')
         elif equipamento == 'acess Point':
            print('ACESS POINT CISCO')
            Meraki_MR33 = 1.000
            Meraki_MR36  =3.700
            Meraki_MR46 = 3.000  
            Meraki_CW9164 = 11.000  
            Meraki_CW9166 = 15.800  
            acesspointcisco = Meraki_MR33 + Meraki_MR36 + Meraki_MR46 + Meraki_CW9164 + Meraki_CW9166

            lista2 = [
               ["Meraki_MR33", "Wi-Fi 5", "870 – 1.000$"],
               ["Meraki_MR36", "Wi-Fi 6", "2.300 – 3.700$"],
               ["Meraki_MR46", "Wi-Fi 6 Enterprise", "3.000 – 4.500$"],
               ["Meraki_CW9164", "Wi-Fi 6E", "11.000 – 12.000$"],
               ["Meraki_CW9166", "Wi-Fi 6E Alta Densidade", "15.800 – 17.000$"],
            ]
            print(tabulate(
               lista2,
               headers=["Modelo Cisco", "Descrição", "Preço médio (R$)"],
               tablefmt="grid"
            ))
      if opção1 == 2:
         print ('Opção 2 selcionada...')
         sleep (1)
         if equipamento == 'roteadores':
                     print ('ROTEADORES TP-LINK')
                     
                     TLWR840N = 114
                     Archer_C50 = 210
                     Archer_AX53 = 260
                     Archer_BE550 = 1.300
                     roteadorestplink = TLWR840N 
                     roteadorestplink1 = Archer_C50
                     roteadorestplink2 = Archer_AX53  
                     roteadorestplink3 = Archer_BE550 = 1.300
                     lista = [

                         ["TLWR840N", "Roteador Wi-Fi N300", "114$"],
                         ["Archer_C50", "Roteador AC1200 Dual Band", "210$"],
                         ["Archer_AX53", "Roteador Wi-Fi 6 AX3000", "260$"],
                         ["Archer_BE550", "Roteador Wi-Fi 7 Tri-Band", "1.300$"],
                        
                     ]
                     print(tabulate(
                        lista,
                        headers=["Modelo TP-LINK", "Descrição", "Preço médio (R$)"],
                        tablefmt="grid"
                     ))
                     equipamentototais = str(input('Deseja escolher um equipamento para calcular o preço total [SIM/NÃO]?'))
                     equipamentoderedetotal = 0
                     if equipamentototais == 'SIM' or equipamentototais == 'sim':
                         equipamentoderede = str(input('Digite aqui o equipamento que deseja:'))
                         equipamentoderedetotal =+ 1
                         if equipamentoderede == 'TLWR840N':
                             print ('voce escolheu {} equipamento e o preço é {}'.format(equipamentoderedetotal, roteadorestplink))
                         elif equipamentoderede == 'ArcherC50':
                             print ('voce escolheu {} equipamento e o preço é {}'.format(equipamentoderedetotal, roteadorestplink1))
                         elif equipamentoderede == 'ArcherAX53':
                             print ('voce escolheu {} equipamento e o preço é {}'.format(equipamentoderedetotal, roteadorestplink2))
                         elif equipamentoderede == 'ArcherBE550':
                             print ('voce escolheu {} equipamento e o preço é {}'.format(equipamentoderedetotal, roteadorestplink3))
                     

                     print ('----------------------------------------------------------------------------------------------')
         elif equipamento == 'switchs':
                     print ('SWITCHS TP-LINK')
                     TLSG105	=	110
                     TLSG108	=	150
                     TLSG1016D	=	553
                     TLSG1024D	=	900
                     TLSG1008MP	=	770
                     T2600G28TS	=	1.359
                     totaisswitchs = TLSG105 + TLSG108 + TLSG1016D + TLSG1024D + TLSG1008MP + T2600G28TS
                     lista1 = [     
                                    ["TLSG105", "Switch Gigabit 5 portas", "110$"],
                                    ["TLSG108", "Switch Gigabit 8 portas", "150$"],
                                    ["TLSG1016D", "Switch Gigabit 16 portas", "553$"],
                                    ["TLSG1024D", "Switch Gigabit 24 portas", "900$"],
                                    ["TLSG1008MP", "Switch Gigabit 8 portas PoE+", "770$"],
                                    ["T2600G-28TS", "Switch Gerenciável L2 24 portas + 4 SFP", "1.359$"]
         
                                    ]
                     print(tabulate(
                              lista1,
                              headers=["Modelo TP-LINK", "Descrição", "Preço médio (R$)"],
                              tablefmt="grid"
                           ))
                     print('----------------------------------------------------------------------------------------------')
         elif equipamento == 'acess Point':
                     print('ACESS POINT TP-LINK')
                     EAP115 =220
                     EAP225 =505
                     EAP610 =720
                     EAP613 =369
                     EAP650 =998
                     totalacesspoint = EAP115 + EAP225 + EAP610 + EAP613 + EAP650

                     lista2 = [

                              ["EAP115", "Access Point N300", "220$"],
                              ["EAP225", "Access Point AC1350 Omada", "505$"],
                              ["EAP610", "Access Point Wi-Fi 6 AX1800", "720$"],
                              ["EAP613", "Access Point Wi-Fi 6 AX1800", "369$"],
                              ["EAP650", "Access Point Wi-Fi 6 AX3000", "998$"],
                     ]
                     print(tabulate(
                        lista2,
                        headers=["Modelo TP-LINK", "Descrição", "Preço médio (R$)"],
                        tablefmt="grid"
                     ))
      if opção1 == 3:
               print ('Opção 3 selcionada...')
               sleep (1)
               if equipamento == 'roteadores':
                           print ('ROTEADORES INTELBRAS')
                           W4_300S= 160
                           W5_1200G= 220
                           W5_1200GS= 250
                           W6_1500 =328
                           R_3000 = 473
                           roteadoresintelbras = W4_300S + W5_1200G + W5_1200GS + W6_1500 + R_3000
                           lista = [   
                                 ["W4_300S", "Roteador Wi-Fi N300", "160$"],
                                 ["W5_1200G", "Roteador Wi-Fi AC1200", "220$"],
                                 ["W5_1200GS", "Roteador Wi-Fi AC1200 Gigabit", "250$"],
                                 ["W6_1500", "Roteador Wi-Fi 6 AX1500", "328$"],
                                 ["RX_3000", "Roteador Wi-Fi 6 AX3000", "473$"],
                              
                           ]
                           print(tabulate(
                              lista,
                              headers=["Modelo intelbras", "Descrição", "Preço médio (R$)"],
                              tablefmt="grid"
                           ))
                           print ('----------------------------------------------------------------------------------------------')
               elif equipamento == 'switchs':
                           print ('SWITCHS INTELBRAS')
                           SF800Q = 80
                           S1116G = 660
                           S1124G = 830
                           S1110G_PA = 875
                           S1120G_PA = 1.903
                           S1128G_PA = 2.633
                           totaisswitchsintelbras = SF800Q + S1116G + S1124G + S1110G_PA + S1120G_PA + S1128G_PA
                           lista1 = [     

                                          ["SF 800 Q+	Switch Fast Ethernet 8 portas	80$"],
                                          ["S1116G	Switch Gigabit 16 portas	660$"],
                                          ["S1124G	Switch Gigabit 24 portas	830$"],
                                          ["S1110G_PA	Switch Gigabit 10 portas PoE	875$"],
                                          ["S1120G_PA	Switch Gigabit 20 portas PoE	1.903$"],
                                          ["S1128G_PA	Switch Gigabit 28 portas PoE	2.633$"],

               
                                          ]
                           print(tabulate(
                                    lista1,
                                    headers=["Modelo intelbras", "Descrição", "Preço médio (R$)"],
                                    tablefmt="grid"
                                 ))
                           print('----------------------------------------------------------------------------------------------')
               elif equipamento == 'acess Point':
                           print('ACESS POINT INTELBRAS')
                           AP_3_10 = 320
                           AP_3_60 = 702
                           AP_12_10_AC = 529
                           AP1250ACMax = 1.006
                           AP1250ACOutdoor = 1.120
                           AP_13_50_AC_S = 890
                           totalacesspoint = AP_3_10 + AP_3_60 + AP_12_10_AC + AP1250ACMax + AP1250ACOutdoor + AP_13_50_AC_S
                           lista2 = [

                                   	["AP_3_10	Access Point Wi-Fi 4 Corporativo	320$"],
                                   	["AP_3_60	Access Point Wi-Fi 4 Longo Alcance	702$"],
                                   	["AP_12_10_AC	Access Point AC1200	529$"],
                                    ["AP1250ACMax	Access Point Wi-Fi 5 Corporativo	1.006$"],
                                   	["AP1250ACOutdoor	Access Point Wi-Fi 5 Outdoor	1.120$"],
                                   	["AP_13_50_AC_S	Access Point Wi-Fi 5 Corporativo	890$"],

                           ]
                           print(tabulate(
                              lista2,
                              headers=["Modelo intelbras", "Descrição", "Preço médio (R$)"],
                              tablefmt="grid"
                           ))       
   if opção == 3:
         equp = int(input('Quantos equipamentos voce deseja calcular?'))
         if equp == 5:
             equip = str(input('Digite o nome do equpamento:')) 
             equip2 = str(input('Digite o nome do equpamento:')) 
             equip3 = str(input('Digite o nome do equpamento:')) 
             equip4 = str(input('Digite o nome do equpamento:')) 
             equip5 = str(input('Digite o nome do equpamento:')) 
             valortotal = equip + equip2 + equip3 + equip4 + equip5
             print ('Os equipamentos são {}, {}, {}, {} e {} o valor total dos equipamentos é {}'.format(equip,equip2,equip3,equip4,equip5,valortotal))

         if equp == 4:
             equip6 = str(input('Digite o nome do equpamento:')) 
             equip7 = str(input('Digite o nome do equpamento:')) 
             equip8 = str(input('Digite o nome do equpamento:')) 
             equip9 = str(input('Digite o nome do equpamento:')) 
             valortotal1 = equip6 + equip7 + equip8 + equip9 
             print ('Os equipamentos são {}, {}, {}, {},  o valor total dos equipamentos é {}'.format(equip6,equip7,equip8,equip9,valortotal1))
         if equp == 3:
             equip10 = str(input('Digite o nome do equpamento:')) 
             equip11 = str(input('Digite o nome do equpamento:')) 
             equip12 = str(input('Digite o nome do equpamento:')) 
             valortotal2 = equip10 + equip11 + equip12
             print ('Os equipamentos são {}, {}, {},  o valor total dos equipamentos é {}'.format(equip10,equip11,equip12,valortotal2))
                  


         if equp == 2:
             equip13 = str(input('Digite o nome do equpamento:')) 
             equip14 = str(input('Digite o nome do equpamento:')) 
             valortotal3 = equip10 + equip11 + equip12
             print ('Os equipamentos são {}, {},  o valor total dos equipamentos é {}'.format(equip13,equip14,valortotal3))
         if equp == 1:
             equip15 = str(input('Digite o nome do equpamento:')) 
             print ('O equipamento é {},o valor total do equipamento é {}'.format(equip15, valortotal3))             
               



    

 