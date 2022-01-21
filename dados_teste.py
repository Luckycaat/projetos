import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./projetos.db")
cursor = conexao.cursor()

# Execução de um comando...
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
      VALUES (12345678900, 'João', '2000-01-31', 1),(11111111111, 'Pedro', '2001-05-07', 1),(22222222222, 'Arthur', '2002-01-28', 0),(33333333333, 'Juan', '2002-01-07', 0);'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()