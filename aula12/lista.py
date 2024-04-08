#          0       2      3
lista = ["Joao","Maria","Pedro"]
print ("Lista original ", lista)

lista.append("José")
print ("Lista com José: ",lista)

tamanho =len(lista)

print  ("Tamanho: ", tamanho)

lista.insert(1, "Matheus")
tamanho = len(lista)
print("Lista com o Matheus ", lista)

nome = lista.pop(2)
print("Lista sem a Maria: ", lista)

lista.remove("Pedro")
pedros = lista.count("Pedro")
print(f"Há {pedros} Pedros na lista")

print("Lista sem o Pedro: ", lista)

for i in range(0, 10):
    lista.append("Joaquim")
print(lista)
joaquim= lista.count ("Joaquim")
print(f"Há {joaquim} Joaquins na lista")

lista.remove("Joaquim")
print(lista)