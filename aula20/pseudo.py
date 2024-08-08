##### Pseudo Codigo para Ler o conteudo de um arquivo CSV ####

### Exemplo de CSV  ==> contatos.csv ####
id; nomes; telefone
0; João Silva; 11111
1; Maria Silva; 22222
3; José Santos; 33333



arq = open('contatos.csv', 'r')
lista = [] 
contador = 0
linha = "-"
while linha != "":          # "id; nomes; telefone"
    linha = arq.readline()  # "0; João Silva; 11111" # Ler proxima linha
                            # ""
    if contador > 0 and linha != "":
        row = linha.split(";")  # ['0', 'João Silva', '11111']


        d = {
            "id": int(row[0]),      # 0
            "nome": row[1]          # "João Silva"
            "telefone": row[2]      # "11111"
        }

        lista.append(d)

        # lista[ {"id": 0, "nome": "João Silva", "telefone": "11111"} ] 
    contador = contador + 1
arq.close()

contato = lista[0]   #   {"id": 0, "nome": "João Silva", "telefone": "11111"}

print( "Id: ", contato["id"])
print( "Nome: ", contato["nome"])
print( "Telefone: ", contato["telefone"])
