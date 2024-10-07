import requests
import json




executando = True
while executando: 
    cidade = input("Digite o nome da cidade a qual deseja saber o horario local: ")

    parametros ={
        "key" : "455671e3300349e6be1122114240710",
        'q' : cidade
    }


    response = requests.get("http://api.weatherapi.com/v1/timezone.json", params=parametros)
    # print(response.content)

    dicionario = json.loads(response.content)
    print(f"O horario atual de {cidade} é {dicionario['location']['localtime']}")