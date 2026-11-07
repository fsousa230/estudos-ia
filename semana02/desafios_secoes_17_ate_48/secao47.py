# Aula 184 - Desafio 31 - Lambda com IF ELSE
# Para este desafio, crie uma função lambda que aceite umm núero e retorne "Par" se o npumnero foir par e "ìmpar" se o número for ímpar

n = int(input('Digite um número: '))

verifica = lambda n: 'Par' if n % 2 == 0 else 'Ímpar'

print(f'O número {n} é {verifica(n)}.')

