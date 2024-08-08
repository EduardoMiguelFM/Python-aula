import os
os.system("cls")

a = 79

# Como pegar este valor da variavel (a)
# como sendo octal

a_em_octal = oct(a)
print("A em octal",a_em_octal)

# Bases numericas
# Algarismos Binarios: 0 ou 1
# Algarismos Octais: 0, 1, 2, 3, 4, 5, 6, 7
# Algarismos Decimais: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Algarismos Hexadecimais: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F

n1 = 8170990732 #8.170.990.732
numero_em_binario = bin(n1)
numero_em_octal =oct(n1)
numero_em_hexadecimal = hex(n1)
print("N1: ",n1)
print("N1 em Binario: ",numero_em_binario)
print ("N1 em octal: ",numero_em_octal)
print ("N1 em hexadecimal: ", numero_em_hexadecimal)

n1      #  8170990732
str(n1) # "8170990732"
print("Habitantes da terra são: "+ str(n1))

f = 971.7234352
i = int(f)
s = str(f)
print("Número Float: ",f)
print("Parte inteira: ",i)
print("Parte Interira: "+ s)

