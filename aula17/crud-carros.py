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
        


def procurar_contato( lista_carro ):
     print("Procurar carro: ")
     print("Informe o placa para pesquisar")
     placa = input()
     indice = 0
     while indice <len(lista_carro):
        carro = lista_carro[indice]
        if carro ["placa"] == placa:
            print("Marca\t\tModelo\t\tAno\t\tplaca")
        print(f"{carro['marca']}\t\t{carro['modelo']}\t\t{carro['Ano']}\t\t{carro['placa']}")

        print("Menu de opções para carro")
        print("(R)Remover")
        print("(A)Alterar")
        print("(V)Voltar ao menu principal")
        opcao = solicita_opcao()
        if opcao == "r":
            del carro[indice]
        elif opcao == "a":
            indice = indice + 1



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