import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./projetos.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
comando = '''CREATE TABLE Marca (
                id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                sigla CHARACTER(2) NOT NULL,
                PRIMARY KEY (id)
                );'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

comando2 = '''CREATE TABLE Veiculo (
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY (placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id)
                );'''

cursor.execute(comando2)

# Efetivação do comando
conexao.commit()

comando3 = '''ALTER TABLE Veiculo
                ADD motor REAL;'''

cursor.execute(comando3)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()