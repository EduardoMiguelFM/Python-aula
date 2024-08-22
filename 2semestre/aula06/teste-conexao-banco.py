import os
import oracledb


usuario =os.environ.get ("FIAP_ORACLE_USER")
senha = os.environ.get ("FIAP_ORACLE_PASS")

con = oracledb.connect (user = usuario,
                        password= senha,
                        dsn="oracle.fiap.com.br:1521/orcl")
print("Database version: ", con.version)




while True:
    os.system("cls")
    cursor = con.cursor()
    print("Menu de opções para acesso ao banco")
    print("(T)Criar Tabela Contatos")
    print("(X)Drop Tabela Contatos")
    print("(I)Inserir um novo contato na Tabela Contatos")
    print("(L)Listar os contatos da Tabela Contatos")
    print("(S)Sair do menu")
    opcao = input("Por favor digite uma opção: ").upper()[0]

    if opcao == "T":
        cursor.execute ("""
            CREATE TABLE Contatos (
                id NUMBER(9) not null,
                nome VARCHAR2(100),
                telefone VARCHAR2(30),
                email VARCHAR2(100),
                CONSTRAINT Contato_pk PRIMARY KEY (id)
    )
    """)
    elif opcao == "X":
        cursor.execute (""""
            ALTER TABLE Contatos DROP CONSTRAINT Contato_pk""")
        
        cursor.execute 
        ("""
        DROP TABLE Contatos
        """)

    elif opcao == "I":
        id = int(input("Informe o Id: "))
        nome = input("Informe o nome do contato: ")
        email = input("Informe o email do contato: ")
        telefone = input("Informe o telefone do contato: ")

        sql = f"""
            INSERT INTO Contatos (id, nome, telefone, email) VALUES (
                       {id}, '{nome}', 
                       '{telefone}', '{email}')
                       """

        cursor.execute(sql, (id, nome, telefone, email,))
      
    elif opcao == 'L':
        print("Listando Contatos:")

        lista = cursor.execute("SELECT * FROM Contatos")
        for row in lista:
            print(row)

    elif opcao == 'S':
        print("Tchau até breve...")
        break
    else:
        print("Opção invalida")

    input("Tecle <ENTER> para continuar")