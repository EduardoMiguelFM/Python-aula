lista = ["Isabela", "Guilherme", "Juliana", "Pablo", "Michael", "Enzo", "Vicenzo", "Guilherme"]

try: 
    pos = lista.index("Guilherme", 2)
    print(f"O Guilherme está na posição: {pos} ")
except:
    print("Elemento não encontrado")

pos = lista.index("Pablo")
print(f"O Pablo está na posição: {pos} ")

try: 
    pos = lista.index("Jõao")
    print(f"O Jõao está na posição: {pos} ")
except ValueError:
    print("Não há João na lista")