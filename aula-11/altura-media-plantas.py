print("Programa para calcular a média de crescimento de uma planta")
qtd_meses = 12
crescimentos = []

for i in range(qtd_meses):
    print(f"Por favor informe o crescimento do mês: {i+1}")    
    cres_mes = float(input())
    crescimentos.append(cres_mes)


soma= 0
for i in range(qtd_meses):
    soma = soma + crescimentos[i]
    

media = soma /qtd_meses
print("Média: ", media)