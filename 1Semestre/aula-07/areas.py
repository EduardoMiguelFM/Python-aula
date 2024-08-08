print("Programa para calcular a area de um retangulo")

while True:

    print("Informe o tamanho da base em centimentro")
    base = float(input())

    print("Informe a altura desse retangulo")
    altura = float(input())

    area = base * altura

    print(f"O tamanho da área é: {area:5.1f} cm")

    print("Você deseja calcular novamente? (S/N)")
    novamente = input()
    if novamente == "N":
        break
print("Fim do programa")
