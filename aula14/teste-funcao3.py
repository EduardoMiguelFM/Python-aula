def area_retangulo( b , a ):
    area = b * a
    return area

def area_triagulo( b = 0 , a = 0 ):
    area = b * a / 2
    return area
#Calcular area de retangulo
#base * altura

#Calcular area de triangulo retangulo
#base * altura / 2
executando = True
while executando: 
    print("PROGRAMA PARA CALCULAR AREAS")

    base = float(input("Informe o valor da base: "))
    altura = float(input("Informe o valor da altura: "))

    menu = """
        Informe o tipo do objeto
        (T)riangulo
        (R)etangulo
    """
    print(menu)
    opcao = input().lower()[0]

    if opcao == "t":
        resultado = area_triagulo(base, altura )

    elif opcao =="r":
        resultado = area_retangulo( base , altura)

    print(" Area é igual a =", resultado)



    print("Deseja (S)air?")
    sair = input().lower()[0]
    if sair == "s":
        executando = False
        print("Fim do programa")
    else :
        executando = True
