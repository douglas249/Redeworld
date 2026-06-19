import math
#pegando informaçoes#
print ('Tem que ter a requisição de equipamentos, por favor digite abaixo os equipamentos:')

computadores = int(input('Quantos compiutadores usará?'))

impressoras = int(input('Quantas impressoras usará?'))

servidordearq = int(input('Quantos servidores de arquivos usará?'))

roteadores = int(input('Quantos roteadores'))
#Fazendo a soma dos componentes para quantidade de conectores RJ45#
cabo1 = computadores * 2
cabo2 = impressoras * 2
cabo3 = servidordearq * 2
cabo4 = roteadores * 2 
#Resposta:#
print ('A quantidade de computadores é {} e a quantidade de conectores para conexão é {}'.format(computadores,cabo1))

print ('A quantidade de impressoras que serão utilizados é {} e a qauntidade de conectores necessários é {}'.format(impressoras, cabo2))

print ('A quantidade de servidores que serão utilizados é {} e a quantidade de conectores necessários é {} '.format(servidordearq, cabo3))

print ('A quantidade de roteadores utilizados é {} e a quantidade de conectores necessários {}'.format(roteadores, cabo4))
#Calculando o tamanho da area e distancia dos equipamentos#
area = int(input('Qual é a quantidade de metros quadrados do seu projeto?'))

distancia = int(input('Qual vai ser a distancia entre os equipamentos?'))
total = distancia * computadores
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




 