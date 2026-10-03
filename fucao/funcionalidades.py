from rich import print

def calcular_valor_equipamento(total_equipamentos):
    quantidade = int(input("Quantos equipamentos você deseja calcular? "))
            
    total = 0
            
    for equipamento in range(quantidade):
                     
        nome = input(f"Digite o nome do {equipamento+1}º equipamento: ")
            
    if nome in total_equipamentos:

            preco = total_equipamentos[nome]  

            print(f"{nome} custa R$ {preco:,.2f}")
    
            total += preco
    else:
        print("[red]Equipamento não encontrado![/]")
            
    print(f"\n[green]Valor totalR$[/]: R$ {total:,.2f}")
