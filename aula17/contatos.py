def menu_usuario():
    print("Menu principal")
    print("(C)Cadastrar")
    print("(L)Listar")
    print("(P)Procurar")
    print("(B)Backup arquivo")
    print("(R)Restaurar arquivo")
    print("(S)Sair")


def solicita_opcao(): #solicita opção para o usario
    print("Escolha sua opcao: ")    
    return input().lower()[0]


def cadastar_contato():
    nome = input("Infome o nome completo do contato: ")
    telefone = input("Informe o Telefone do contato: ")
    email= input("Informe o E-mail do contato: ")
    peso = float(input("Informe o peso do contato: "))
    d = {"nome": nome, "telefone": telefone, "email": email, "peso": peso}
    return d


def listar_contatos( lista_contato ):
    indice = 0
    while indice <len(lista_contato):
        contato = lista_contato[indice]
        print("Nome\t\tTelefone\t\tEmail\t\tPeso")
        print(f"{contato['nome']}\t\t{contato['telefone']}\t\t{contato['email']}\t\t{contato['peso']}")
        indice = indice + 1


def procurar_contato( lista_contato ):
     print("Procurar contato: ")
     print("Informe o email para pesquisar")
     email = input()
     indice = 0
     while indice <len(lista_contato):
        contato = lista_contato[indice]
        if contato ["email"] == email:
            print("Nome\t\tTelefone\t\tEmail\t\tPeso")
        print(f"{contato['nome']}\t\t{contato['telefone']}\t\t{contato['email']}\t\t{contato['peso']}")

        print("Menu de opções para contato")
        print("(R)Remover contato")
        print("(A)Alterar contato")
        print("(V)Voltar ao menu principal")
        opcao = solicita_opcao()
        if opcao == "r":
            del contato[indice]
        elif opcao == "a":
            indice = indice + 1
        


lista = []
executando = True

while executando:
    print(" -----------Programa de gestão de contatos-----------")
    menu_usuario()
    opcao = solicita_opcao()
    if opcao == "c":
        contato = cadastar_contato()
        lista.append( contato )

    elif opcao == "l":
        listar = listar_contatos()

    elif opcao == "p":
        procurar = procurar_contato()
        
    elif opcao == "s":
        print("Obrigado por usar o nosso sistema, volte logo!")
        executando = False
print("Tecle <ENTER> para continuar")
input()