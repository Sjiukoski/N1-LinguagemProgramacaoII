class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)

    def aumentaSalario(self):
        self.salario += 20
        print(f'Programador - Nome: {self.nome}, idade: {self.idade} anos. \nO novo salário é: ${self.salario} reais')

class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)

    def aumentaSalario(self):
        self.salario += 30
        print(f'Analista - Nome: {self.nome}, idade: {self.idade} anos. \nO novo salário é: ${self.salario} reais')

class Teste:
    def mostraResultado(self):
        programador = Programador('Mike Wallace',66, 4000)
        analista = Analista('Richard miller',33, 5500)

        programador.aumentaSalario()
        analista.aumentaSalario()

resultado = Teste()
resultado.mostraResultado()