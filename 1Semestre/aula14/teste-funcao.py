def somar_lista(): 
    soma = 0
    for numero in lista :
        soma = soma + numero
    return soma


lista = [1, 2, 3, 4, 5, 6,]

executando = True
while executando:
    print("P R O G R A M A  P A R A  C A L C U L A R  S O M A  E  M E D I A ")
    menu = """ 
        Calcular a (S)oma da Lista  
        Calcular a (M)edia da lista 
        (X)Sair
    """
    print(menu)
    opcao = input().upper()[0]

    if opcao =="S":
        s = somar_lista()
        print ("Soma: ",s)

    elif opcao =="M":
        s = somar_lista()
        media = s / len(lista)
        print("Media: ", media)

    elif opcao =="X":
        print("Até breve")
        executando = False
print("Fim do programa")