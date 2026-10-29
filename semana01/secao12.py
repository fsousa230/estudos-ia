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
'''valores = [50, 80, 110, 150, 180]

for x in valores:
    print(f'O valor final do produto é de R$ {x}')'''

#Aula 81 - Verificando itens em uma lista
'''cor_cliente = input('Digite a cor desejada: ')
cores = ['Amarelo', 'Verde', 'Azul', 'Vermelho']

if cor_cliente.lower() in cores:
    print('Em estoque')
else:
    print('Não temos esta cor em estoque')'''

#Aula 82 - Agregando duas listas com o Zip
'''cores = ['Amarelo', 'Verde', 'Azul', 'Vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)
print(list(duas_listas))'''

#Aula 83 - Input em uma lista
# Criar uma lista de frutas a partir do input fornecido pelo usuário
'''frutas_usuario = input('Digite o nome das frutas separados por vírgula')

frutas_lista = frutas_usuario.split(', ')

print(frutas_lista)'''

#Aula 84 - Entendendo sobre Tuples
'''cores_list = ['Amarelo', 'Verde', 'Azul', 'Vermelho']
cores_tuple = ('Amarelo', 'Verde', 'Azul', 'Vermelho') #TUPLE utiliza PARENTESES ao invés de COLCHETES. E também não conseguimos editar as TULPLES

print(type(cores_list))
print(type(cores_tuple))'''

#Aula 85 - Trabalhando com Arrays
'''from array import array

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])


print(letras)
print(numeros_i)
print(numeros_f)'''

#Aula 86 - Criando Sets
# Set: similar as listas; Evita itens duplicados; não utiliza index
'''list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union
print(num1 - num2) # Difference
print(num1 ^ num2) # Symmetric Difference
print(num1 & num2) # And

print(len(num1))'''

#Aula 87 - Funções em Sets
'''list1 = [1, 2, 3, 4, 5, 6]
s1 = {1, 2, 3, 4, 5, 6} # Set é criado com CHAVES
s1.add(7)
s1.update([8, 9, 10]) # acrescenta vários valores de um vez, tem que inserir como lista
s1.remove(10) # Remove gera um erro caso não encontre o valor a ser removido
s1.discard(90)

print(list1)
print(s1)
print(type(list1))
print(type(s1))'''

#Aula 88 - Sets com strings
'''set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
print(set4)
set4 = set1.difference(set2)
print(set4)
set4 = set1.intersection(set2)
print(set4)
set4 = set1.symmetric_difference(set2)
print(set4)'''

#Aula 89 - Introdução a Dicionários
# Utiliza index no formato de Keys e Values
# Aceita string, integer, float, boolean...
'''aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}
print(aluno)
print(aluno['nome'])
print(aluno['idade'])'''

#Aula 90 - Atualizando itens no dicionário
'''aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

aluno['nome'] = 'Jose'
print(aluno)
aluno.update({'nome': 'Jose', 'nota_final': 'B'}) # com o Update conseguimos alterar mais de um informação ao mesmo tempo
print(aluno)
aluno.update({'endereco': 'Rua A'}) # com o Update conseguimos acrescentar mais informações
print(aluno)
print(aluno.get('sobrenome', 'Não existe')) # com o GET podemos colocar uma mensagem para dados não encontrados
del aluno['idade']
print(aluno)'''

#Aula 91 - Looping dentro de um dicionário
'''aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

for x in aluno.items():
    print(x)
for keys, values in aluno.items():
    print(f'Descrição: {keys} - Valor: {values}')'''

#Aula 92 - Visualizando Itens, Keys e Values
'''aluno = {'nome': 'Ana',
         'idade': 16,
         'nota_final': 'A',
         'aprovacao': True,
         'Materias': ['Física', 'Matematica', 'Ingles']
         }
print(aluno)
print(aluno.get('Materias'))
print(len(aluno))
print()
print(aluno.items())
print(aluno.keys())
print(aluno.values())'''

#Aula 93 - Conhecendo a Função Lambda
# É uma função (pequena) sem nome
# Pode ter vários argumentos mas somente uma expressão
# Muito utilizada dentro de outras funções
# Código mais 'clean'
'''def somar(x):
    return x + 10
print(somar(2))


somar10 = lambda x, y: x + y + 10
print(somar10(2, 4))'''

#Aula 94 - Lambda dentro de uma função
'''def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4
print(somar(2))'''

#Aula 95 - Função Map em uma lista
# Muito utilizado com listas
# Aplicar uma função a um Interable, por item (list, tuple, dic, etc)
'''lista1= [1, 2, 3, 4]

def multi(x):
    return x * 2


lista2 = map(multi, lista1)
print(list(lista2))'''

#Aula 96 - Função Map com Labda
'''lista1= [1, 2, 3, 4]

#def multi(x):
#   return x * 2


#lista2 = map(lambda x: x * 2, lista1)
print(list(map(lambda x: x * 2, lista1)))'''

#Aula 97 - Função Filter
# Muito utilizado com listas
# Aplicar uma função a um Interable, filtrando os items. (list, tuple, dic, etc)
'''valores = [10, 12, 34, 44, 57]
def remover20(x):
    return x> 20

print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores)))'''
           
#Aula 98 - Entendendo List Comprehension com strings
# Mais simples de se escrever
# Utilizado quando você precisa criar uma nova lista a partir de uma existente
# [expressão for iten in itens]
'''frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
#frutas2 = []

#for iten in frutas1:
#    if 'n' in iten:
#        frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if 'n' in iten]

print(frutas2)'''

#Aula 99 - Entendendo List Comprehension com números
'''#valores = []

#for x in range(6):
#    valores.append(x * 10)

#print(valores)

valores = [x * 10 for x in range(6)]
print(valores)'''

#Aula 100 - Lista e Generator Expressions
# Uma forma mais rápida para listas, dicionários e etc
# Menos memória alocada
# Valores em Bytes
from sys import getsizeof

numeros = [x * 10 for x in range(100000)]
print(type(numeros))
print(getsizeof(numeros))

print('__________')

numeros = (x * 10 for x in range(100000))
print(type(numeros))
print(getsizeof(numeros))