quantidade = int(input('digita ai'))


for espaco in quantidade:
        area = int(input('Qual é a quantidade de metros quadrados do seu projeto?'))
        distancia = int(input('Qual vai ser a distancia entre os equipamentos?'))
        total = distancia * espaco
        espaco_total = area + total

        for area_total in range(distancia):


            print(f'A área total do seu projeto é {espaco_total}m²')