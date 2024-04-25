lista = [
    {"nome" : "Jõao Silva", "tel": "1111", "email": "joao@teste.com"},
    {"nome" : "Maria Silva", "tel": "2222", "email": "Maria@teste.com"},
    {"nome" : "Roberto", "tel": "3333", "email": "Roberto@teste.com"},
    {"nome" : "Paulo", "tel": "4444", "email": "Paulo@teste.com"}
]

arq1 = open("./contatos.csv", "w", encoding="utf-8")
# o1 = {"nome" : "Jõao Silva", "tel": "1111", "email": "joao@teste.com"}
# arq1.write(o1["nome"] + ", "+ o1["tel"]+ ", " + o1 ["email"])


#cabecalho
arq1.write("Nome, Telefone, Email")

for contato in lista:
    arq1.write(contato["nome"] + ", "+ contato["tel"]+ ", " + contato ["email"])
    arq1.write("\n")
arq1.close()