lista = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17]

# Forma que o resultado deste filtro, contenha apenas os numeros que forem diviseis por 3 ou por 4

def filtro_div_3_ou_4 (numero):
    return numero % 3 == 0 or numero % 4 == 0 

nova_lista = filter(filtro_div_3_ou_4, lista)

print("Lista og: ")
print(lista)

print("Lista de numeros divisiveis por 3 ou 4")
print(list(nova_lista))






