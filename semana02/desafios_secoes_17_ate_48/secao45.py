# Aula 180 - Desafio 29 - Convertendo para Lambda
# Para este desafio, crie uma função lambda que aceite um número e retorne o cubo desse número.

numero = int(input('Digite um número: '))

cubo = lambda n: n ** 3
print(f'O cubo de {numero} é {cubo(numero)}')