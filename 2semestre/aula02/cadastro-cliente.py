clientes = [
    {"nome": "João Silva", "idade": 24,"genero": "M"},
    {"nome": "Maria Silva", "idade": 37,"genero": "F"},
    {"nome": "Alberto Roberto", "idade": 55,"genero": "M"},
    {"nome": "Iracema Souza", "idade": 70,"genero": "F"}
]

filtro_masculino = lambda dicionario :  dicionario ["genero"] == "M"

homens =  filter(filtro_masculino, clientes)

print("Todos os clientes:")
print(clientes)

print("Apenas homens:")
print(list(homens))

filtro_feminino = lambda dicionario : dicionario ["genero"] == "F"

mulheres =  filter(filtro_feminino,clientes)

print("Apenas mulheres")
print(list(mulheres))