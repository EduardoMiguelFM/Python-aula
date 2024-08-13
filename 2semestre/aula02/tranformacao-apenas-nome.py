import os 
os.system ("cls")

clientes = [
    {"nome": "João Silva", "idade": 24,"genero": "M"},
    {"nome": "Maria Silva", "idade": 37,"genero": "F"},
    {"nome": "Alberto Roberto", "idade": 55,"genero": "M"},
    {"nome": "Iracema Souza", "idade": 70,"genero": "F"}
]

tranforma_nomes = lambda d: d["nome"]

lista_nomes = map(tranforma_nomes, clientes)

print("Clientes: ")
print(clientes)

print("Apenas os nomes:")
print(list(lista_nomes))