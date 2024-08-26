import os
import oracledb


usuario =os.environ.get ("PYTHON_ORACLE_USER")
senha = os.environ.get ("PYTHON_ORACLE_PASS")
db_path="oracle.fiap.com.br:1521/orcl"


con = oracledb.connect (user = usuario,
                        password= senha,
                        dsn= db_path )


ddl_pet = """
CREATE TABLE pet(
    id_pet NUMBER(10) CONSTRAINT id_pet_pk PRIMARY KEY,
    nm_pet VARCHAR2(50) CONSTRAINT nm_pet_nn NOT NULL,
    raca_pet VARCHAR2(20) CONSTRAINT raca_pet_nn NOT NULL,
    nm_tutor VARCHAR(100) CONSTRAINT nm_tutor_pet_nn NOT NULL
)
"""

cursor = con.cursor()
cursor.execute(ddl_pet)
con.commit()
print("Tabela foi criada")


# print("---------Olá Cadastre o seu PET aqui---------")
# id_pet = int(input("Digite o id do seu pet: "))
# nm_pet = input("Digite o nome do seu pet: ")
# raca_pet input("Digite a raça do seu pet: ")
# nm_tutor input("Digite o nome do tutor: ")

# sql = """
# INSERT INTO pet (id_pet, nm_pet, raca_pet, nm_tutor)
# VALUES ({id_pet}, {nm_pet}, {raca_pet}, {nm_tutor})
# """