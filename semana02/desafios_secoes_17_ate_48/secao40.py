# Aula 170 - Desafio 24 - Funções Simples
# Crie uma função que aceite um número como entrada e retorna o quadrado desse número

def quadrado(n):
    return n * n

numero = int(input('Digite um número: '))
print(f'O quadrado do número {numero} é {quadrado(numero)}')