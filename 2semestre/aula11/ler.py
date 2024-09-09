import requests 
import json

url = 'https://tdspm-2ad2e-default-rtdb.firebaseio.com/contatos.json'

response = requests.get (url)

texto = response.text

# print("Responde: ", response)
# print("Corpo: ", texto)

contatos = json.loads(texto)

# print("Chave dos contatos")
# for chave in contatos.keys():
#     print(chave)

for contato in contatos.values():
    print(f"Nome:{contato['nome']}, \tEmail: {contato['email']}")