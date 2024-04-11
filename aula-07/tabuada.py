print("Programa da tabuada")

print("Digite um numero para eu fazer a tabuada")
num = int(input())

                #inicialização       termino        incremento

for i  in range(1,                   11,            1):
    res = num * i
    print(f"{num} X {i:>2} = {res:>2} ")