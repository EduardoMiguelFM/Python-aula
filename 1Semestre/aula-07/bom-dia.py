print("Programa para dar bom dia")
executar = True
while executar == True:
    print("Digite o seu nome")
    nome = input()
    print("Bom dia", nome)
    print("Você deseja continuar (S/N)" )
    continuar = input()
    if continuar == "N":
        executar = False
