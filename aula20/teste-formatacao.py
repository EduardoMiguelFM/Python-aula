lancamentos = [
    {"lancamento": "Pagamento recebido, valor": 2419.90},
    {"lancamento": "Posto Shell, valor": 55.00},
    {"lancamento": "Mc Donalds, valor": 38.99}
]


for lancamento in lancamentos:
    print("{0}\t\tR${1:91f}".format(lancamento['lancamento'],lancamentos))