# Aula 132 - Desafio 5 - Criando listas
# Neste desafio, quero que você crie um script que solicite ao usuário dois números. 
# Em seguida, seu script deve imprimir a soma, a subtração, a multiplicação, a divisão (resultado decimal)
# e a exponenciação (primeiro número elevado ao segundo número) desses dois números.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
exponenciacao = n1 ** n2

print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')
print(f'Exponenciação: {exponenciacao}')