# ADICIONEI ALGUMAS BIBLIOTECAS PARA MELHORAR O PROGRAMA#  

from rich import print
from time import sleep

from fucao import interface
from fucao import listaderepeticao
from fucao import funcionalidades






#LISTA DE EQUIPAMENTOS PARA CALCULOR DE VALOR NA OPÇÃO 3#

   
#ROTEADORES CISCO#
roteadorescisco1 = [
    
     ["ISR_1100", 2500],
     ["ISR_4321", 5600],
     ["ISR_4331", 7000],
     ["ISR_4431", 15000]
]


switchscisco2 = [
      
   #SWITCHS CISCO#
   ["Catalyst_C1200_24T_4G", 2790],
   ["Catalyst_C1200_24P_4G", 4000],
   ["Catalyst_C1200_48P_4G", 59309]
]

acesspointscisco3 = [
      
   #ACEESS POINTS CISCO#
   ["Meraki_MR33", 1.035],
   ["Meraki_MR36", 3.765],
   ["Meraki_MR46", 3.000],
   ["Meraki_CW9164", 11000],
   ["Meraki_CW9166", 15878] 

]

roteadoreTPLINK1 = [
      
   #ROTEADORES TP LINK#
   ["TLWR840N", 114],
   ["Archer_C50", 210],
   ["Archer_AX53", 260],
   ["Archer_BE550", 1300]
]

switchTPLINK2 = [
      
   #SWITCHS TP LINK#
   ["TLSG105", 1100],
   ["TLSG108", 1500],
  ["TLSG1016D", 553],
   ["TLSG1024D", 900],
   ["TLSG1008MP", 770],
   ["T2600G28TS", 1359]
   
]

acesspointTPLINK3 = [
      
   #ACESS POINTS TP LINK#
   ["EAP115", 220],
   ["EAP225", 505],
   ["EAP610", 720],
   ["EAP613", 369],
   ["EAP650", 998]
]

roteadoresINTELBRAS1 = [ 
   ["W4_300S",  160],
   ["W5_1200G", 220],
   ["W5_1200GS",250],
   ["W6_1500",  328],
   ["RX_3000",  473]
   ]

switchINTELBRAS2 = [
      
    #SWITCHS INTELBRAS#
   ["SF800Q", 80],
   ["S1116G", 660],
   ["S1124G", 830],
   ["S1110G_PA", 875],
   ["S1120G_PA", 1.903],
   ["S1128G_PA", 2.633]
]

acesspointINTELBRAS3 = [
      
    #ACESS POINTS INTELBRAS#
   ["AP_3_10", 320],
   ["AP_3_60", 702],
   ["AP_12_10_AC", 529],
   ["AP1250ACMax", 1.006],
   ["AP1250ACOutdoor", 1.120],
   ["AP_13_50_AC_S", 890]
   
]

#essa lista recebe as demais lista dos equipamentos, utilzo as listas para receber os equipamentos porque assim consigo mostra-los mais facilmente na opão 2#
lista_total_equipamentos = [acesspointINTELBRAS3, switchINTELBRAS2, roteadoresINTELBRAS1,   
                           acesspointTPLINK3, switchTPLINK2, roteadoreTPLINK1, 
                           acesspointscisco3, switchscisco2, roteadorescisco1]



roteadorescisco = {
    
     "ISR_1100": 2500,
     "ISR_4321": 5600,
     "ISR_4331": 7000,
     "ISR_4431": 15000
}


switchscisco = {
      
   #SWITCHS CISCO#
   "Catalyst_C1200_24T_4G": 2790,
   "Catalyst_C1200_24P_4G": 4000,
   "Catalyst_C1200_48P_4G": 59309
}

acesspointscisco = {
      
   #ACEESS POINTS CISCO#
   "Meraki_MR33": 1.035,
   "Meraki_MR36": 3.765,
   "Meraki_MR46": 3.000,
   "Meraki_CW9164": 11000,
   "Meraki_CW9166": 15878 

}

roteadoreTPLINK = {
      
   #ROTEADORES TP LINK#
   "TLWR840N": 114,
   "Archer_C50": 210,
   "Archer_AX53": 260,
   "Archer_BE550": 1300
}

switchTPLINK = {
      
   #SWITCHS TP LINK#
   "TLSG105": 1100,
   "TLSG108": 1500,
  "TLSG1016D": 553,
   "TLSG1024D": 900,
   "TLSG1008MP": 770,
   "T2600G28TS": 1359
   
}

acesspointTPLINK = {
      
   #ACESS POINTS TP LINK#
   "EAP115": 220,
   "EAP225": 505,
   "EAP610": 720,
   "EAP613": 369,
   "EAP650": 998
}

roteadoresINTELBRAS = { 
   "W4_300S":  160,
   "W5_1200G": 220,
   "W5_1200GS":250,
   "W6_1500":  328,
   "RX_3000":  473

   }

switchINTELBRAS = {
      
    #SWITCHS INTELBRAS#
   "SF800Q": 80,
   "S1116G": 660,
   "S1124G": 830,
   "S1110G_PA": 875,
   "S1120G_PA": 1.903,
   "S1128G_PA": 2.633
}

acesspointINTELBRAS = {
      
    #ACESS POINTS INTELBRAS#
   "AP_3_10": 320,
   "AP_3_60": 702,
   "AP_12_10_AC": 529,
   "AP1250ACMax": 1.006,
   "AP1250ACOutdoor": 1.120,
   "AP_13_50_AC_S": 890
   
}

#ESSA VARIAVEL RECEBE TODOS OS DICIONARIOS ACIMA DOS EQUIPAMENTOS, UTILIZEI DICIONARIOS PARA CONSEGUIR PERCORRER CADA LISTA UTILIZANDO NOMES NA OPÇÃO 3#
dicionario_equipamentos = [acesspointINTELBRAS, switchINTELBRAS, roteadoresINTELBRAS,   
                           acesspointTPLINK, switchTPLINK, roteadoreTPLINK, 
                           acesspointscisco, switchscisco, roteadorescisco]

      



#TODOS EQUIPAMENTOS E PREÇOS#

# CHAMANDO A FUNÇÃO DE APRESENTAÇÃO
interface.cabecalho()
sleep(1)

opcao = 0

#UMA ESTRUTURA DE REPETIÇAO, REPETE AS OPÇÃO#
while opcao != 4:
#DENTRO DO WHILE LEVA 4 OPÇOES QUE SE ORGANIZADAS POR IFS, CADA IF EM SUA RESPECTIVA OPÇAO LEVA UMA FUNCAO DENTRO, CHAMANDO AS FUNCIONALIDADES DE DA OPÇAO DESEJADA#
   interface.opcoes_escolha('[blue][ 1 ][/] calcular quantidade de conectores e caixas de rede.\n\n'
    '[blue][ 2 ][/] ver listagens de preço de equipamentos atual.\n\n'   '[blue][ 3 ][/] Calcular os preços entre os equipamentos.\n\n'  '[blue][ 4 ][/] Salvar e encerrar.')
   
   while True:
      try:
         opcao = int(input('Qual opção deseja?'))
      except ValueError:
          print('[red]ERRO![/] Digite um valor inteiro para selecionar a opção')
      else:
          break

#NA OPÇAO 1 LEVA A FUNCAO ESCOLHENDO EQUIPAMENTOS#
   if opcao == 1:

      print('Opção 1 selcionada, [green]vamos calcular[/]!...')
      sleep (1)
      #FUNCAO QUE FICA RESPOSANVEL POR FAZER A ESCOLHA DOS EQUIPAMENTOS, COLOQUEI CADA VARIAVEL PARA QUE RECEBEM OS VAALORES QUE FOREM RETORNADAS DA FUNCAO#
      equipamento, quantidade_equipamento, area, caixas = listaderepeticao.escolhendo_equipamento()


   #NA OPÇAO 2 LEVA UMA FUNCAO ONDE UTILIZA A LISTA DE EQUIPAMENTOS PARA MOSTRAR OS EQUIPAMENTOS DIPONIVEIS#
   if opcao == 2:
      
      interface.opcoes_escolha('[ 1 ] Cisco System\n\n'  '[ 2 ] TP-Link\n\n' '[ 3 ] Intelbras\n\n')

      opcao1 = int(input('Escolha uma marca: '))

      if opcao1 == 1:
            print ('Opção [green]1[/] selcionada...')
            sleep (1)

            interface.painel_de_equipamento(roteadorescisco1, switchscisco2, acesspointscisco3)
         
      if opcao1 == 2:
         print ('Opção [green]2[/] selcionada...')
         sleep (1)

         interface.painel_de_equipamento(roteadoreTPLINK1, switchTPLINK2, acesspointTPLINK3)
         
      if opcao1 == 3:
               print ('Opção [green]3[/] selcionada...')
               sleep (1)

               interface.painel_de_equipamento(roteadoresINTELBRAS1, switchINTELBRAS2, acesspointINTELBRAS3)

   #NA OPÇAO 3 COLOQUEI UMA VARIAVEL PARA RECEBER AS INFORMACOES QUE FOREM RETORNADAS DA FUNCAO, ESSA FUNCAO UTILIZA O DICIONARIO DE EQUIPAMENTOS#       
   if opcao == 3:
#RESPOTA DA LISTA DE EQUIPAMENTOS:

      valor_total = funcionalidades.calcular_valor_equipamento(dicionario_equipamentos)
      
   #OPÇAO 4 É RESPOSANVEL POR RECBER TODAS AS VARIAVEIS QUE RECEBEM OS VALORES DAS FUNCOES OS GUARDA E CRIAR UMA TABELA E SALVA NO BANCO DE DADOS#     
   if opcao == 4:
      from fucao.banco_dados import BancoDeDados
      banco = BancoDeDados()
      dados_projeto = {
                  "equipamento": equipamento,
                  "quantidade_equipamento": quantidade_equipamento,
                  "area": area,
                  "caixas": caixas,
                  "valor_total": valor_total    }
      
      interface.opcoes_escolha('[ 1 ] Criar e salvar projeto\n\n' '[ 2 ] Ver projetos salvos') 

      escolha = int(input('Qual opção deseja?'))

      if escolha == 1:
         sleep(1)
         banco.criar_banco()
         banco.salvar_dados(dados_projeto)
         print('[green]Dados salvos com sucesso![/]')

      if escolha == 2:
         resultado = banco.ver_projetos()

         for equipamento,equipamento_quantidade, area, caixas, valor_total in resultado:
            print(f'Equipamento: {equipamento}')
            print(f'Quantidade: {equipamento_quantidade}')
            print(f'Área: {area}')
            print(f'Caixas do projeto: {caixas}')
            print(f'Valor do projeto {valor_total}R$')
              

    

 