import os
from datetime import datetime

import oracledb

class Contato():
    """
        Classe de contato para servir como padrão para os objetos
    """
    nome =""
    telefone=""
    email=""
    nascimento = datetime.now()


def menu():
        os.system("cls")
        print("--------- M E N U ---------")

        print("(G)erar a tabela no banco de dados")
        print("(C)adastrar")
        print("(L)er Registro")
        print("(S)air")
    
    

def inserir_opcao():
    opcao = input("Por Favor digite uma opção: ")
    opcao_filtrada =  opcao.lower()[0]
    if opcao_filtrada in ['g','c', 'l', 's']:
        return opcao_filtrada
    
    else:
        print("Opção inválida, tecle <ENTER> para prosseguir")
        input()


def gerar_conexao_db():
    usuario =os.environ.get ("FIAP_ORACLE_USER")
    senha = os.environ.get ("FIAP_ORACLE_PASS")
    db_path="oracle.fiap.com.br:1521/orcl"


    con = oracledb.connect (user = usuario,
                            password= senha,
                            dsn= db_path )
    return con



def gravar_db (contato: Contato)-> bool:
    conexao = gerar_conexao_db()
    cursor = conexao.cursor()
    sql = """INSERT INTO agenda (nome, telefone, email, nascimento)
             VALUES (:1, :2, :3, :4)
    
    """
    try:
        cursor.execute (sql)
        conexao.commit()
    except Exception as err:
         print("Erro: ",err)
         conexao.rollback()
         return False

    conexao.close()
    return True
     

def gerar_tabela() -> bool:
    conexao = gerar_conexao_db()
    cursor = conexao.cursor()

    sql = """CREATE TABLE agenda(
            nome varchar2(100) CONSTRAINT agenda_nome_pk PRIMARY KEY,
            telefone varchar2(20) CONSTRAINT agenda_telefone_nn NOT NULL,
            email varchar2(50) CONSTRAINT agenda_email_nn NOT NULL,
            nascimento DATE)
    """
    try:
        cursor.execute(sql)
        conexao.commit()
    except Exception as err:
        print("Erro: ", err)
        conexao.rollback()
        return False
    finally:
        conexao.close()
        
    return True



def cadastrar() -> Contato:
    
    """
         Função para pedir os dados de contato, e retorna um objeto do tipo Contato
    """

    os.system("cls")
    print("---------Cadastro de Contato---------")
    nome = input("Informe o nome: ")
    telefone = input("Telefone: (DD)XXXXX-XXXX: ")
    email = input("Email: XXXXX@YYYY.ZZZ:  ")
    nascimento = input("Nascimento: DD/MM/YYYY:  ")

    if  len(nome) > 5 and \
        len(telefone) > 5 and \
        len(email) > 5 and len(nascimento) == 10:
         date_format = "%d/%m/%Y"
         nascimento_date = datetime.strptime(nascimento, date_format)

    if nascimento_date >= datetime.now():
            contato = Contato()
            contato.nome = nome
            contato.telefone = telefone
            contato.email = email
            contato.nascimento = nascimento_date
            return contato
    else:
        print("Data de nascimento incorreta")
    return None



if __name__ == "__main__":
    executando = True
    while executando:
        menu()
        opcao = inserir_opcao()
        print(f"O usuario escolheu, {opcao}")

        if opcao == "c":
            contato = cadastrar()
            if contato is not None:
                pass
                gravar_db( contato)
            else:
                print("Contato inválido")
            
        elif opcao == "s":
            executando = False
            print("Tchau até breve!")
        input("Telece <ENTER> para continuar")
