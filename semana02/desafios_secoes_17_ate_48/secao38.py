# Aula 166 - Desafio 22 - Pesquisa de País e Capital
# Para este desafio, crie uma lista com 5 nomes de países e as capitais desses países.
# Peça ao usuário para digitar o nome de um país. Se o país estiver na lista, imprima "A capital de [país] é [capital]".
# Se o país não estiver na lista, imprima "Desculpe, não temos informações sobre a capital desse país".

lista = {'Brasil':'Brasília', 'Itália':'Roma', 'Japão':'Tokyo'}
pais = input('Digite o nome de um país: ')
if pais in lista:
    print(f'A capital de {pais} é {lista[pais]}.')
else:
    print('Desculpe, não temos informações sobre a capital desse país.')