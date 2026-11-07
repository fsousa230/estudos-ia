# Aula 174 - Desafio 26 - Calculado base e exponente
# Para este desafio, crie uma função que calcule a potência de um número. A função deve aceitar dois argumentos: a base e o expoente.
# No entanto, se o expoente não for fornecido ao chamar a função, ele deve assumir o valor padrão de 2.

def potencia(b, e=2):
    print(f'A potência é: {b ** e}')

base = int(input('Digite o valor da base: '))
expoente = input('Digite o expoente: ')

if expoente:
    potencia(base, int(expoente))
else:
    potencia(base)