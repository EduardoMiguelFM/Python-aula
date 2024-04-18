linha1 = ""
caractere = "#"
for j in range(0, 8):
    for i in range(0, 5):
        linha1 += caractere
    caractere = " " if caractere == "#" else "#"


caractere = " "    
linha2 = ""
for j in range(0, 8):
    for i in range(0, 5):
        linha2 += caractere
    caractere = " " if caractere == "#" else "#"


print(linha1)