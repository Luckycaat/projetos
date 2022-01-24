class Pessoa:
    def __init__(self, cpf, nome, data_nascimento, usa_oculos):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.usa_oculos = usa_oculos
        self.veiculos = []

class Marca:
    def __init__(self, id, nome, sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla

class Veiculo:
    def __init__(self, placa, ano, cor, motor, proprietario, marca):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.proprietario = proprietario
        self.marca = marca


def recuperar_veiculos(conexao, cpf):
    # Aquisição de cursor
    cursor = conexao.cursor()

    # Definição dos comandos
    comando = '''SELECT * FROM Veiculo
                 JOIN Marca ON Marca.id = Veiculo.marca
                 WHERE Veiculo.proprietario = ?;'''
    cursor.execute(comando, (cpf,))

    # Recuperação dos registros
    veiculos = []
    registros = cursor.fetchall()
    for registro in registros:
        marca = Marca(*registro[6:])
        veiculo = Veiculo(*registro[:5], marca)
        veiculos.append(veiculo)

    # Fechamento do cursor
    cursor.close()
    return veiculos