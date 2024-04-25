arquivo1 = open("./nomes.txt","r",encoding="utf-8")

texto = arquivo1.readline()
print(texto)

texto = arquivo1.readline()
print(texto)

arquivo1.close()