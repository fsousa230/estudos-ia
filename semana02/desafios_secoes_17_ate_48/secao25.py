# Aula 140 - Desafio 9 - Removendo itens da lista
# Para este desafio, comece com a lista 'frutas' do desafio anterior. Primeiro, remova a 'manga' da lista usando o método remove().
# Depois disso, remova o último item da lista usando o comando del. # Por fim, imprima a lista modificada na tela.

frutas = ['maçã', 'banana', 'manga', 'uva']

print(frutas)

frutas.remove('manga')
del frutas[-1]

print(frutas)