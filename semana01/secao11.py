#Aula 66 - De Functions a Libraries
# Somente introdução e explicações sobre Function, Module, Package e Library

#Aula 67 - Como funciona uma função
#  Explicação de como funciona

#Aula 68 - Criando uma função
'''def boas_vindas():
    print('Olá Felipe')
    print('Temos 5 laptops em estoque')

boas_vindas()'''

#Aula 68 - Criando uma função de soma
'''def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)


def multiplicar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 * numero2
    print(resultado)


somar_dois_numeros()
multiplicar_dois_numeros()'''

#Aula 69 - Parâmetros e Argumentos em uma função
'''def boas_vindas_Marcos():
    print('Olá Marcos')
    print('Temos 5 laptops em estoque')


def boas_vindas_Ronaldo():
    print('Olá Ronaldo')
    print('Temos 4 laptops em estoque')


def boas_vindas_Maria():
    print('Olá Maria')
    print('Temos 2 laptops em estoque')


boas_vindas_Marcos()
boas_vindas_Ronaldo()
boas_vindas_Maria()


def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')


boas_vindas(input('Nome: '), input('Quantidade: '))'''

#Aula 70 - Argumentos Default e Non-default
# Parametro = Argumento
# Default = Aquele que você define o valor no parametro
# Non-default = Aquele que você não define o valor no parametro
# Importante: se você vai definir algum parametro default ele tem SEMPRE que vir APÓS os argumentos non-default

'''def boas_vindas(nome, quantidade=6):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')


boas_vindas('Marcos')'''

#Aula 71 - Print ou Return em Funções
'''def cliente1(nome):
    print(f'Olá {nome}.')


def cliente2(nome):
    return f'Olá {nome}.'


x = cliente1('Maria')
y = cliente2('Jose')

print(x)
print(y)'''

#Aula 72 - Vários argumentos xargs com números
# Criar uma função que soma vários números
'''def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado +=num
    return resultado


x = soma(2,3,4,7)

print(x)'''


#Aula 73 - Vários argumentos cargs nomeando parametros
# Criar uma função que armazena números e strings (dados)
'''def agencia(**carro):
    return carro


print(agencia(modelo='Gol', cor='Branco', motor=1.0, placa=1234))
print(agencia(modelo='Palio', cor='Preto', motor=1.6))
print(agencia(modelo='Voyage', cor='Cinza',))'''

#Aula 74 - Importanto um módulo
import math

print(math.factorial(4))

fatorial = 4 * 3 * 2 * 1
print(fatorial)

