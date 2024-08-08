import os
os.system("cls")

s= "Ola Mundo !!!"
print ("Texto: "+ s)

s_minusculo = s.lower() #ola mundo
s_maiusculo = s.upper() #OLA MUNDO
print("Texto minusculo: "+ s_minusculo)
print("Texto maiusculo: "+ s_maiusculo)

tamanho = len( s )
print("Ola mundo: ", tamanho)
print("Tamanho da string: "+ str(tamanho))

#        01234567890123456789012345678901
texto = "A FIAP é uma faculdade bem legal"
tam = len(texto)
print("Tamanho: ", tam)
letra = texto[17]
print("Letra na posição 17 é: "+ letra)
letra = texto[20]
print("Letra na posição 20 é: "+ letra)

pos = texto.find ("legal")
print("O texto possui a palavra legal na posição: ",pos)

pos = texto.find ("m",)
print("O texto possui a letra m na posição: ",pos)

pos = texto.find ("m", 11  )
print("O texto possui outra letra m na posição: ",pos)

pos = texto.find ("m", 26  )
print("O texto possui outra letra m na posição: ",pos)


a= 20 + 30
print("O valor é: ", a)

b= str(30)
print("O valor do numero é", b)

c= 898908
numero_hexadecimal= hex(c)
print("Numero em hexadecimal", numero_hexadecimal)

texto= "Ola mundo"
d= len(texto)
print(d)

#e= int

f= "PROVA PROFII"
pos = f.find("P", 1)
print("A posição do P é: ",pos)