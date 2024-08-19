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

    match opcao:
        case "+":
            soma = somar(n1,n2)
            print(f"O resultado da soma é: {soma} ")

        case "-":
            sub = subtrair(n1,n2)
            print(f"O resultado da subtração é: {sub}")

        case "*":
            multi = multiplicar(n1,n2)
            print(f"O resultado da multiplicação é: {multi}")

        case  "/":
            div = dividir(n1,n2)
            print(f"O resultado da multiplicação é: {div}")
    
 
    