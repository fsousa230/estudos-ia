#Exercicio 1
"""nome = input('Nome: ')
idade = int(input('Idade: '))

print(f'Olá, {nome}, você tem {idade} anos.')"""

#Exercicio 2
"""n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

media = (n1+n2+n3) / 3

if media >= 7:
    print(f'Média de {media}. Você está aprovado!')
else:
        print(f'Média de {media}. Você está reprovado!')"""

#Exercicio 3
"""for numero in range(1,21):
      verificanumero = numero % 2

      if verificanumero == 0:
            print(numero)"""

#Exercicio 4
"""soma = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 0:
        print(f'A soma de todos os numeros que digitou foi: {soma}')
        break
    else:
        soma = soma + numero"""

#Exercicio 5
"""resto = 17 % 5
inteira = 17 // 5
potencia = 2 ** 10

print(f'O resto da divisão 17 por 5 é: {resto}')
print(f'O inteiro da divisão 17 por 5 é: {inteira}')
print(f'E 2 elevado a 10 é: {potencia}')"""

#Reforço A
"""for numero in range(1,11):
    print(numero)"""

#Reforço B
"""numero = 10
for contagem in range(1,11):
    print(numero)
    numero -=1"""
#Reforço C
"""print('Tabuada do 7')
numero = 1
for tabuada in range(1,11):
    print(f'7 x {numero} = {7 * numero}')
    numero += 1"""

#Desafio opcional
numero = int(input('Digite um número: '))

print(f'Tabuada do {numero}:')

for multiplicador in range(1,11,+1):
    print(f'{numero} x {multiplicador} = {numero * multiplicador}')