# Aula 152 - Desafio 15 - Contador de lista
# Para este desafio, crie uma lista de frutas que inclui "maçã" três vezes e outras frutas de sua escolha.
# Use um loop for para contar quantas vezes "maçã" aparece na lista e imprima o resultado.

frutas = ['maçã', 'banana', 'maçã', 'manga', 'maçã', 'uva']

contador = 0

for f in frutas:
    if f == 'maçã':
        contador += 1

print(f'A palavra "maçã" aparece {contador} vezes na lista.')