try:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))  
    resultado = n1/n2
    print(f"A divisão de {n1} por {n2} é igual a {resultado}")

except ValueError as err: 
    print("Erro ! Digite um número válido")

except ZeroDivisionError as err: 
    print("Erro! segundo número precisa ser diferente de (0) zero")
except:
    print("Erro! não foi possivel executar a divisão")