# Aula 178 - Desafio 28 - Duas funções
# Para este desafio, crie duas funções. A primeira função deve aceitar um número e retornar o dobro desse número.
# A segunda função deve aceitar um número e retornar o quadrado desse número.
# Em seguida, chame a primeira função dentro da segunda para retornar o quadrado do dobro de um número.

def dobro(n):
    return n * 2


def quadrado(n):
    return n * n


numero = int(input('Digite um número: '))
print(f'Número {numero}. O dobro dele é: {dobro(numero)}; Ele ao quadrado é: {quadrado(numero)}; E o quadrado do dobro dele é: {quadrado(dobro(numero))}.')