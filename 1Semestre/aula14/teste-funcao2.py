lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [10, 20, 30, 40, 50, 60]


def somar_lista( lista_origem ): 
    soma = 0
    for numero in lista_origem :
        soma = soma + numero
    return soma



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
        s = somar_lista( lista2 )     #somar os valores da lista2
        print ("Soma: ",s)

    elif opcao =="M":
        s = somar_lista( lista1 )      #fazer a media com os valores da lista1
        media = s / len(lista1)    
        print("Media: ", media)

    elif opcao =="X":
        print("Até breve")
        executando = False
print("Fim do programa")