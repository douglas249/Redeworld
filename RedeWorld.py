import math
from time import sleep
print ('Bem vindo ao RedeaWorld, aqui voce poderá calcular a quantidade de conectores RJ45 e caixas de cabo de rede para o seu prjeto!')
sleep(1)
opção = 0
while opção != 5:
   print ( '[ 1 ] calcular quantidade de conectores e caixas de rede\n'  '[ 2 ] ver listagens de preço de equipamentos atual\n'  '[ 3 ] Salvar e encerrar')
   opção = int(input('Qual opção deseja?'))
   if opção == 1:
      print ('Opão 1 selcionada, vamos calcular!...')
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
   



    