'''
Inicio do programa
'''


texto = "Digite um numero: "
valido = False

while  not valido:
    print (texto)
    digitado = input()
    try:
        numero=int(digitado)
        valido = True
    except:
         print("O número é invalido")
print("Numero digitado: ",numero)







'''
Fim do programa
'''