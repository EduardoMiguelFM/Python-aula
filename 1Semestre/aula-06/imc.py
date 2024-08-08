import os
os.system("cls")

print("Bem vindo(a) à calcuculadora de IMC")

altura = float(input("Informe a sua altura em metros: "))
peso = float(input("Informe o seu peso: "))
imc = (peso/(altura**2))

if altura <0 or altura >400 :
    print("A altura iformada está errada!")

print(f"O seu IMC é: {round(imc, 2)}")

if imc <= 16.9 and imc >=0.1 : 
    print("Você está muito abaixo do peso")
elif imc <= 17 and imc >=18.4 : 
    print("Você está abaixo do peso")
elif imc >= 18.5 and imc <=24.9 : 
    print("O seu peso está ideal")
elif imc >= 25 and imc <=29.9 : 
    print("Você está levemente acima do peso")
elif imc >= 30 and imc <=34.9 : 
    print("Você tem obesidade grau I")
elif imc >= 35 and imc <=40 : 
    print("Você tem obesidade grau II")
else :
    print("Você tem obesidade grau III")

