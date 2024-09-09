import requests 

url = 'https://tdspm-2ad2e-default-rtdb.firebaseio.com/contatos.json'

contato ={ "nome": "Alberto Santos", 
           "telefone": "(13) 5555-5555",
           "email": "albertosantos@gmail.com"
           }

response = requests.post( url, json=contato )

print(response)

