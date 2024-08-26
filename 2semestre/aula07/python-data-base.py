import os
import oracledb


usuario =os.environ.get ("PYTHON_ORACLE_USER")
senha = os.environ.get ("PYTHON_ORACLE_PASS")
db_path="oracle.fiap.com.br:1521/orcl"


con = oracledb.connect (user = usuario,
                        password= senha,
                        dsn= db_path )

print("Database version: ", con.version)

ddl_times_futebol = """
CREATE TABLE times_futebol(
    id_time NUMBER(10) CONSTRAINT id_times_futebol_pk PRIMARY KEY,
    nm_time VARCHAR2 (60) NOT NULL,
    jogadores NUMBER (5) NOT NULL,
    vitorias NUMBER (5) NOT NULL,
    derrotas NUMBER (5) NOT NULL,
    empates NUMBER (5) NOT NULL
)
"""

cursor = con.cursor()
cursor.execute(ddl_times_futebol)
con.commit()




print("Tabela foi criada")