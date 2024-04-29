def menu_usuario():
    print("Menu principal")
    print("(C)Cadastrar")
    print("(L)Listar")
    print("(P)Procurar")
    print("(S)Sair")


def carro_cadastar( lista_carro ): #cadastra o carro
    carro = {}
    carro ["marca"]= input("Informe a marca do carro: ")
    carro ["modelo"]= input("Informe o modelo do carro: ")
    carro ["ano"]= input("Informe o ano do carro: ")
    carro ["placa"]= input("Informe a placa do carro: ")
    lista_carro.append(carro) #adiciona as informações dada pelo usuario a uma lista

def carro_listar (lista_carro): #lista todos os carros cadastrados
    for p in lista_carro:
        print(f"Marca do carro: ", p["marca"], "\nModelo do carro: ", p["modelo"], "\nAno do carro: ", p["ano"], "\nPlaca do carro: ", p["placa"])
        

def solicita_opcao(): #solicita opção para o usario
    print("Escolha sua opcao: ")    
    return input().lower()[0]


lista = []
executando = True

while executando:
    menu_usuario()
    opcao = solicita_opcao()
    if opcao == "c":
        cadastrar = carro_cadastar(lista)
    elif opcao == "l":
        listar = carro_listar(lista)
    elif opcao == "s":
        print("Obrigado por usar o nosso sistema, volte logo!")
        executando = False