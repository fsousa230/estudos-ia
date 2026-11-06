# Aula 158 - Desafio 18 - Procura em listas
# Para este desafio, imagine que você tem uma loja de carros. Crie uma lista com os carros que você tem em estoque: BMW X6, BMW i5, BMW i8.
# Peça ao usuário para que ele insira o nome do carro que deseja comprar. Se o carro estiver em estoque, imprima "Este carro está disponível".
# Se o carro não estiver em estoque, imprima "Desculpe, este carro não está disponível".

carros = ['BMW X6', 'BMW i5', 'BMW i8']

comprar = input('Qual carro deseja comprar? ')

if comprar in carros:
    print('Este carro está disponível.')
else:
    print('Este carro não está disponível.')

    