print ("********** Calculadora de Média final **********")

executar =True

while executar == True:
    print("Escreva o nome do seu aluno: ")
    aluno = input()

    print("Por favor escreva a primeira nota do aluno: ")
    nota1 = float(input())

    print("Por favor escreva a segunda nota do aluno: ")
    nota2 = float(input())

    print("Por favor escreva a terceira nota do aluno: ")
    nota3 = float(input())

    mediaFinal = (nota1 + nota2 + nota3)  /3

    print("Nome            Nota1        Nota2         Nota3           Media")
    print(f"{aluno:<12}{nota1:<9.1f}{nota2:>9.1f}{nota3:<9.1f}{mediaFinal:<11.1f}")

    print("Deseja fazer o calculo com outro aluno? (S/N)")
    res = input()
    if res == "N" and "n":
        break
print("Fim do programa")

