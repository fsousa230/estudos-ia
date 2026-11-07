# Aula 182 - Desafio 30 - Lambda multiplicando
# Para este desafio, crie uma função lambda que aceite dois números e retone a multiplicação desses números

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

multiplicacao = lambda n1, n2: n1 * n2
print(f'{n1} x {n2} = {multiplicacao(n1,n2)}')