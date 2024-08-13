import os 
os.system ("cls")

vendas = [120, 80, 150, 90, 200]

# filra as vendas acima de 100
acima_100 = lambda acima : acima > 100
acima_100 = list(filter(acima_100, vendas))


print("Produtos acima de 100: ")
print(list(acima_100))

print("")

# Aplica um desconto de 10% para as vendas acima de 100
desconto = lambda desc : desc * 0.9
desconto = map(desconto , acima_100)

print(list(desconto))
