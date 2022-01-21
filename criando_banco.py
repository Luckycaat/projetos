import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./projetos.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
comando = '''CREATE TABLE Pessoa (
                cpf INTEGER NOT NULL,
                nome TEXT NOT NULL,
                nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL,
                PRIMARY KEY (cpf)
                );'''

cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()