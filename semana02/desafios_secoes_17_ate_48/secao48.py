# Aula 186 - Desafio 32 - Lambda com for loop
# Para este desafio, cria uma função lambda que eleve um número ao quadrado. Em seguida, use essa função para calcular o queadrado de todos
# os números em uma lista usando um loop for.

quadrado = lambda n: n * n

lista = [1, 2, 3, 4]
resultados = []
for numero in lista:
    resultados.append(quadrado(numero))

print(f'Os quadrados dos números {lista} são {resultados}')