import sqlite3 as conector
from contextlib import closing
from modelo import *

conexao = conector.connect("./projetos.db")
cursor = conexao.cursor()

comando = '''SELECT * FROM Pessoa;'''
cursor.execute(comando)
pessoas = []
reg_pessoas = cursor.fetchall()

for reg_pessoa in reg_pessoas:
    pessoa = Pessoa(*reg_pessoa)
    pessoa.veiculos = recuperar_veiculos(conexao, pessoa.cpf)
    pessoas.append(pessoa)
    
for pessoa in pessoas:
    print(pessoa.nome)
    for veiculo in pessoa.veiculos:
        print('\t', veiculo.placa, veiculo.marca.nome)
    
# Fechamento das conexões
cursor.close()
conexao.close()
