'''
    M E N U  P R I N C I P A L 


(C)adastrar Nova (B)icicleta
Cadastrar (U)suario
(C)alcular seguro
(L)istar Usuarios
Listar B(I)cicletas

'''
executar =True
while executar:
    print ("Início do programa")

    print(   " M E N U  P R I N C I P A L ")
    print("\n\n")
    print ("Cadastrar Nova (B)icicleta")
    print ("Cadastrar (U)suario")
    print ("(C)alcular seguro")
    print ("(L)istar Usuarios")
    print ("Listar B(I)cicletas")
    print("(S)air")

    print ("Infore a opção desejada: ")
    opcao = input().upper()[0]

    if opcao == "B":
        print("Você escolheu a opção Cadastrar da bicicleta")
    elif opcao == "U": 
        print ("Você escolheu a opção Cadastrar usuário")
    elif opcao =="C":
        print ("Você escolheu a opção Calcular seguro")
    elif opcao =="L":
        print ("Você escolheu a opção Listar seguro")    
    elif opcao =="I":
        print ("Você escolheu a opção Listar Bicicletas")
    elif opcao =="S":
        print ("Até breve")
        executar = False
        print ("Fim do programa")
        
    else:
        print("Opção invalida, digite novamente:")