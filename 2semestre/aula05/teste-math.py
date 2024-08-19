
#Crinado uma função para o menu de opcoes
def menu():
    print("M E N U  D E  O P C O E S ")
    print("(C)adastrar")
    print("(M)ostrar")
    print("(R)emover")
    print("(A)tualizar")
    print("(S)air")

#criando uma funcao para o usuario selecionar uma opcao
def solicita_opcao():
    print("Selecione uma opcao:")
    return input().lower()[0] 

#Programa principal (Main) que vai rodar o codigo, utilizando um laço while
executar = True
while executar:
    print("----Teste Match----")

    menu()
    opcao = solicita_opcao()
    match opcao:
        case "c":
            print("Você selecinou Cadastrar")
        case "m":
            print("Você selecinou Mostrar")
        case "r":
            print("Você selecinou Remover")
        case "a":
            print("Você selecinou Atualizar")
        case "s":
            print("Você selecinou Sair")
        case _:
            print("Opção invalida")

    


    
