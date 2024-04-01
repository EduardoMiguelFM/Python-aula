linhas=int(input("Informe a quantidade de linhas: "))
colunas=int(input("Informe a quantidade de colunas: "))


for i in range (0, linhas):
    for j in range(0, colunas):
        print(j+1, end="")
    print("")
    