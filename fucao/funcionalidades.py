from rich import print

def calcular_valor_equipamento(total_equipamentos):

    """ESSA FUNÇÃO RECEBE O DICIONARIO DE EQUIPAMENTOS E CALCULA O VALOR TOTAL DE TODOS OS EQUIPAMENTOS ESCOLHIDOS PELO USUARIO. FICA NA OPÇAO 3 DO SISTEMA PRINCIPAL"""
    while True:
        try:

            quantidade = int(input("Quantos equipamentos você deseja calcular? "))

        except ValueError:

            print('[red]ERRO![/] Digite um número inteiro válido.')

        else:

            break

    total = 0

    for valor in range(quantidade):
        while True:

            nome = input(f"Digite o nome do {valor + 1}º equipamento: ").strip().lower()

            if not nome:

                print('[red]Digite o nome do equipamento![/]')

            else:

                break

        encontrado = False


        for dicionario in total_equipamentos:

            if nome in dicionario:

                encontrado = True

                preco = dicionario[nome]

                total += preco

                print(f"{nome} custa R$ {preco:,.2f}")


        if not encontrado:

            print("[red]Equipamento não encontrado![/]")

    print(f"\n[green]Valor total:[/] R$ {total:,.2f}")

    return total_equipamentos, total
