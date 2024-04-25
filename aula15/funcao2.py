def recebe_numero( texto="Digite um número: " ):
    '''
    Função utilizada para pedir numero inteiro,
    e verifica o valor se o valor digitado é um número válido
    '''

    valido = False
    while  not valido:
        print (texto)
        digitado = input()
        try:
            numero=int(digitado)
            valido = True
        except:
            print("O número é invalido")
    return numero
   

print("Início do programa")
n1 = recebe_numero("Digite o 1 numero: ")
n2 = recebe_numero("Digite o segundo numero: ")
soma = n1 + n2
print("Resultado da soma entre os dois números: ",soma)
print("Fim do programa")