lista = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17]

# Forma que o resultado deste filtro, contenha apenas os numeros que forem diviseis por 3 ou por 4

filtro = lambda numero : numero % 3 == 0 or numero % 4 == 0    

print("Teste do filtro com numero 16: ", filtro(16))

nova_lista = filter(filtro, lista)

print("Lista og: ")
print(lista)

print("Lista de numeros divisiveis por 3 ou 4")
print(list(nova_lista))

