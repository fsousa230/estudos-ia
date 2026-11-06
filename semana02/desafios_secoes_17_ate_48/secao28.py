# Aula 146 - Desafio 12 - Nested For Loop
# Para este desafio, crie uma lista de frutas e outra de vegetais. Use um "for loop" aninhado (Nested for loop) 
# para imprimir todas as combinações possíveis de frutas e vegetais, com a fruta primeiro e o vegetal em segundo

frutas = ['maçã', 'banana', 'manga', 'uva']
vegetais = ['alface', 'cenoura', 'abobrinha', 'brócolis']

for f in frutas:
    for v in vegetais:
        print(f'{f} com {v}')