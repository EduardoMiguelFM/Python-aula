import os
import oracledb


usuario =os.environ.get ("PYTHON_ORACLE_USER")
senha = os.environ.get ("PYTHON_ORACLE_PASS")
db_path="oracle.fiap.com.br:1521/orcl"


con = oracledb.connect (user = usuario,
                        password= senha,
                        dsn= db_path )

print("---------Olá Cadastre o seu PET aqui---------")
id = int(input("Digite o id do seu pet: "))
nome = input("Digite o nome do seu pet: ")
raca = input("Digite a raça do seu pet: ")
tutor = input("Digite o nome do tutor: ")

sql = ("""
INSERT INTO pet (id_pet, nm_pet, raca_pet, nm_tutor)
VALUES (?, ?, ?, ?,)
""", (id,nome,raca,tutor))


cursor = con.cursor()
cursor.execute(sql)
con.commit()
print("Registro inserido")
