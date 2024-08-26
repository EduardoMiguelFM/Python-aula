import os
import oracledb


usuario =os.environ.get ("PYTHON_ORACLE_USER")
senha = os.environ.get ("PYTHON_ORACLE_PASS")
db_path="oracle.fiap.com.br:1521/orcl"


con = oracledb.connect (user = usuario,
                        password= senha,
                        dsn= db_path )


sql = """
    INSERT INTO times_futebol (id_time,nm_time,jogadores,vitorias,derrotas,empates)
    VALUES(1,'Santos', 30, 11, 6, 6)
"""


# sql = """
#     INSERT INTO times_futebol (id_time,nm_time,jogadores,vitorias,derrotas,empates)
#     VALUES(2,'São Paulo', 30, 16, 5, 3)
# """


# sql = """
#     INSERT INTO times_futebol (id_time,nm_time,jogadores,vitorias,derrotas,empates)
#     VALUES(3,'Real Madrid', 30, 1, 0, 1)
# """

cursor = con.cursor()
cursor.execute(sql)
con.commit()
print("Registro inserido")

