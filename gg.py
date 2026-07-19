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