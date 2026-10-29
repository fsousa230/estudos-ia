#Aula 59 - For Loop - Separando Strings
#Separar qualquer coisa por espaços
#esse end no final da linha 5 nada mais é que a solicitação pro programa continuar imprimindo na mesma linha as letras
'''palavra = 'FANTASTICO'
for space in palavra:
    print(f' {space}' , end='')'''

#Aula 60 - For Loop - Criando um Retangulo
'''linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()'''

#Aula 61 - Conhecendo While o Loop
#Criar loop para sempre no dia seguionte o produto entrar em promoção até chegar no valor de compra e minimo para parar a promoção
'''valor = 100
dia =1

while valor > 20:
    print(f'Dia {dia}: R$ {valor}')
    valor -=5
    dia +=1'''

#Aula 62 - Operador Ternário
#Modo simplificado do if else, o que teria mais ou menos 4 linhas se transformou em apenas uma
'''idade = 15

resultado = 'Voto Permitido' if idade >= 16 else 'Voto não permitido'
print(resultado)'''

#Aula 63 - Diferenças entre For Loop e While Loop
'''
if e else = verificar verdadeiro ou falso
for = quando você sabe até onde vai a repetição
while = quando você não sabe até onde vai a repetição
'''

#Aula 64 - Criando condições com While Loop
#Publicar um produto com comissão de 10% se for acima de R$ 20
'''valor = int(input('Digite o valor do seu produto: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de R$ {valor}')
    break'''
