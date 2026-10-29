#Aula 75 - Introdução a Listas
# Lista = Armazena mais de uma informação em variáveis
# Mantém a sequência dos dados em uma variável
'''cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', "Salvador"]

print(cidades)'''

#Aula 76 - Manipulando Listas
'''cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
#               0               1              2        3

print(cidades[-2])
print(cidades[0])

cidades[0] = 'Brasilia'
print(cidades[0])'''

#Aula 77 - Funções dentro de listas
'''cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
#               0               1              2        3

print(cidades)

cidades.append('Brasilia')
print(cidades)
cidades.remove('Rio de Janeiro')
print(cidades)
cidades.insert(1, 'Santa Catarina')
print(cidades)
cidades.pop(2)
print(cidades)
cidades.sort()
print(cidades)'''

#Aula 78 - Concatenando listas
'''numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

numeros.extend(letras)
print(numeros)

#                   0               1
itens = [['Item 1', 'Item 2'], ['Item 3']]
#            0          1           0

print(itens[1])
print(itens[0])
print(itens[0][1])'''

#Aula 79 - Extraindo variáveis de listas
'''produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7, 8]
#index         0        1          2         3

item1, item2, item3, *outros, item8 = produtos

print(item1)
print(item2)
print(item3)
print(outros)
print(item8)'''

#Aula 80 - Looping dentro de uma lista
valores = [50, 80, 110, 150, 180]

for x in valores:
    print(f'O valor final do produto é de R$ {x}')

#Aula 81 - Verificando itens em uma lista
#Aula 82 - Agregando duas listas com o Zip
#Aula 83 - Input em uma lista
#Aula 84 - Entendendo sobre Tuples
#Aula 85 - Trabalhando com Arryas
#Aula 86 - Criando Sets
#Aula 87 - Funções em Sets
#Aula 88 - Sets com strings
#Aula 89 - Introdução a Dicionários
#Aula 90 - Atualizando itens no dicionário
#Aula 91 - Looping dentro de um dicionário
#Aula 92 - Visualizando Itens, Keys e Values
#Aula 93 - Conhecendo a Função Lambda
#Aula 94 - Lambda dentro de uma função
#Aula 95 - Função Map em uma lista
#Aula 96 - Função Map com Labda
#Aula 97 - Função Filter
#Aula 98 - Entendendo List Comprehension com strings
#Aula 99 - Entendendo List Comprehension com números
#Aula 100 - Lista e Generator Expressions