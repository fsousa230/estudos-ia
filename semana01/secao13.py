#Aula 101 - O que são erros
# Explicação de alguns erros que podem ser tratados no Phyton
# Erros são excelentes para testes
# Não realiza o 'stop' no programa
# Mensagens customizadas quando encontra um erro

#Aula 102 - Trabalhando com o Try e Except com uma lista
'''try: 
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')'''

#Aula 103 - Trabalhando com o Try e Except com o input
'''try:
    valor = int(input('Digite o valor do seu produto: R$ '))
    print(f'Valor do produto: R$ {valor}')
except ValueError:
    print('Favor digitar um valor em números!')'''

#Aula 104 - Adicionando o Else e Finally
try:
    valor = int(input('Digite o valor do seu produto: R$ '))
    print(f'Valor do produto: R$ {valor}')
except ValueError:
    print('Favor digitar um valor em números!')
#else:
#    print('Usuário digitou um valoor correto')
#    resultado = valor * 2
#    print(resultado)
finally:
    print('Código ok.')