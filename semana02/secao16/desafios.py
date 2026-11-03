# Aula 116 - Desafio com IF, ELIF, ELSE
'''Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto do cozimento em portugues. O usuário deverá fornecer a temperatura
Temperatura - Cozimento
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passada)
'''
'''temperatura = int(input('Qual é a temperatura da carne? '))

if temperatura < 48:
    print('Cozinhar por mais alguns minutos')
elif temperatura >= 48 and temperatura <= 53:
    print('Selada')
elif temperatura >= 54 and temperatura <= 59:
    print('Ao ponto para o mal')
elif temperatura >= 60 and temperatura <= 64:
    print('Ao ponto')
elif temperatura >= 65 and temperatura <= 70:
    print('Ao ponto para o bem')
else:
    print('Bem passada')'''


# Aula 118 - Desafio com Funções - Calculadora para Pintura
'''Crie um programa que calcule a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguintes informações: rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'
'''
'''rendimento = float(input('Qual é o rendimento da lata? '))
altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))

def cal_lata(rend, alt, larg):
    return (alt * larg) / rend

print(f'Você necessita de {cal_lata(rendimento, altura, largura)} latas de tinta.')'''

#  Aula 120 - Desafio com Sets - Filtrando funcionários em um empresa
'''Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:
Lista 1 = Funcionários que têm carro e trabalham durante a noite
Lista 2 = Funcionários que têm carro e trabalham durante o dia
Lista 3 = Funcionários que não têm carro
'''
'''funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)'''

# Aula 122 - Desafio IF e ELIF - Calculo de IMC
'''Calculo de IMC - Índice de Massa Corporal

Qual sua altura em cm: 
Qual seu peso em kg: 

MENOR QUE 18,5 - MAGREZA
ENTRE 18,5 E 24,9 - NORMAL
ENTRE 25,0 E 29,9 - SOBREPESO
ENTRE 30,0 E 39,9 - OBESIDADE
MAIOR QUE 40,0 - OBESIDADE GRAVE
'''

altura = float(input('Qual sua altura em cm? '))
peso = float(input('Qual seu peso em kg? '))

def cal_imc(a, p):
    return p / (a / 100)**2

imc = cal_imc(altura, peso)

if imc < 18.5:
    print('MAGREZA')
elif imc >= 18.5 and imc <= 24.9:
    print('NORMAL')
elif imc >= 25.0 and imc <= 29.9:
    print('SOBREPESO')
elif imc >= 30.0 and imc <= 39.9:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')