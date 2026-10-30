#Seção 14: OOP (Python Object-Oriented Programming)

#Aula 105 - Conhecendo Classes
# São utilizadas para criar Objetos (instances)
# Objetos são partes dentro de uma Class (instancias)
# Classes são utilizadas para agrupar dados e funções, podendo reutilizar
# Ex: Class = Frutas; Objects: Abacate, Banana...

#Aula 106 - Criando a primeira Classe
'''class Funcionarios:
    nome = 'Elena'
    sobrenome = 'Cabral'
    data_nascimento = '12/01/2009'

usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)'''

#Aula 107 - Criando objetos dentro de uma Classe
# Criar a classe
'''class Funcionarios:
    pass

# Criar o onjeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

# Criar os parâmetros do usuário 1
usuario1.nome = 'Elena'
usuario1.sobrenome = 'Cabral'
usuario1.data_nascimento = '12/01/2009'

# Criar os parâmetros do usuário 2
usuario2.nome = 'Marcos'
usuario2.sobrenome = 'Silva'
usuario2.data_nascimento = '15/10/2005'

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)
print(usuario2.nome)
print(usuario2.sobrenome)
print(usuario2.data_nascimento)'''

#Aula 108 - Criando Construtores
'''class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

# Criar o onjeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Marcos', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Gabriel', 'Lima', '01/01/2001')

print(usuario1.nome)
print(usuario2.nome)
print(usuario3.nome)'''

#Aula 109 - Adicionando mais funções à Classe
'''class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

# Criar o onjeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Marcos', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Gabriel', 'Lima', '01/01/2001')

print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario2))'''

#Aula 110 - Calculando a idade do funcionário
from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# Criar o onjeto
usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Marcos', 'Silva', 2005)
usuario3 = Funcionarios('Gabriel', 'Lima', 2001)

print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
print(Funcionarios.idade_funcionario(usuario3))

