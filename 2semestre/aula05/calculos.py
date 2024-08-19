def somar (n1,n2):
    soma = n1 + n2
    return soma

def subtrair (n1,n2):
    sub =  n1 - n2
    return sub

def multiplicar (n1,n2):
    multi = n1 * n2
    return multi

def dividir (n1,n2):
    div  = n1 / n2
    return div

def solicita_opcao():
    print("Selecione uma opcao ( + | - | * | / )")
    return input()[0]

if __name__ == "__main__":
    n1 = float(input("Digitar o primeiro numero: "))
    n2 = float(input("Digitar o segundo numero:"))

    opcao = solicita_opcao()

    if opcao == "+":
        soma = somar(n1,n2)
        print(f"O resultado da soma é: {soma} ")

    elif opcao == "-":
        sub = subtrair(n1,n2)
        print(f"O resultado da subtração é: {sub}")

    elif opcao == "*":
        multi = multiplicar(n1,n2)
        print(f"O resultado da multiplicação é: {multi}")

    elif opcao == "/":
        div = dividir(n1,n2)
        print(f"O resultado da multiplicação é: {div}")
    
 
    