# Aula 162 - Desafio 20 - Par e Impar
# Para este desafio, crie uma lista de números de 1 a 10. Use um 'for loop' para iterar sobre a lista.
# Se o número atual da iteração for par, imprima "O número [número] é par".
# Se o número for ímpar, imprima "O número [número] é ímpar".

lista = list(range(1,11))
for i in lista:
    if i % 2 == 0:
        print(f'O número {i} é par.')
    else:
        print(f'O número {i} é ímpar.')