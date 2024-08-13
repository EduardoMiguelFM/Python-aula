# função deve receber 1 ou 2 parametros, evitar 3 ou + parametros
# 

lista = [1,2,3,4,5,6,7,8,9,10]


# Numeros impares
for numero in lista:
    if numero % 2 != 0:
        print(numero)

print("----------------------")

# Impares ao quadrado
for numero in lista:
    if numero % 2 != 0:
        quadrado = numero * numero
        print(quadrado)