lista = ["Ola","joao","maria","jose","abraao","Tchau"]

match lista:

    case [cumprimento, *nomes, saida]:
        for nome in nomes:
            print(cumprimento, nome)
