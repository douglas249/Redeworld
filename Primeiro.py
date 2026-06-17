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
area = int(input('Qual é a qauntidade de metros quadrados do seu projeto?'))
distancia = int(input('Qual vai ser a distancia entre os entre os equipamentos?'))
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
