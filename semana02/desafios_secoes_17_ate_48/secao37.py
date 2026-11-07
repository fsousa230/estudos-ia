# Aula 164 - Desafio 21 - Lista de Cidades
# Para este desafio, crie uma lista com os nomes de três cidades.
# Peça ao usuário para digitar o nome de uma cidade. Se a cidade estiver na lista, imprima "A cidade está na lista de cidades".
# Se a cidade não estiver na tupla, imprima "A cidade não está na lista de cidades".

# Obs. Você não pode utilizar list[ ]

cidades = ('São Paulo', 'Rio de Janeiro', 'Salvador')
cidade = input('Digite o nome de uma cidade: ')

if cidade in cidades:
    print(f'A cidade {cidade} está na lista.')
else:
    print(f'A cidade {cidade} não está na lista.')