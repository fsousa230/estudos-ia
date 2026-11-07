# Aula 172 - Desafio 25 - Soma com funções
# Para este desafio, crie uma função que aceite dois números como entrada e retorne a soma desses números

def soma(n1, n2):
    print(f'{n1} + {n2} = {n1 + n2}')


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma(n1,n2)