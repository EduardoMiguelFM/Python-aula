print("Programa para calcular a média aritimética de 3 notas de um aluno")
lista = []

for i in range(3):
    print(f"Por favor digite a {i+1} nota: ")
    n = float(input())
    lista.append(n)

soma = 0
for i in range(3):
    numero = lista[i]
    soma = soma + numero
    print("Número: ",numero, "\tSoma: ",soma)
media = soma / 3
print ("A média final é: ", media)