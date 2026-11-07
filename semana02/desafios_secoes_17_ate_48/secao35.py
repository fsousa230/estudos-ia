# Aula 160 - Desafio 19 - Encontrando um item com While
# Para este desafio, crie um loop que peça ao usuário para digitar o nome de uma fruta.
# Se a fruta digitada não for 'abacate', o loop deve continuar pedindo ao usuário para digitar o nome de uma fruta.
# Se a fruta for 'abacate', o loop deve terminar e o programa deve imprimir "Parabéns, você acertou a fruta!".

fruta = ''
while fruta != 'abacate':
    fruta = input('Digite o nome de uma fruta: ')
    print(f'Fruta digitada: {fruta}')

print('Parabéns, você acertou a fruta!')