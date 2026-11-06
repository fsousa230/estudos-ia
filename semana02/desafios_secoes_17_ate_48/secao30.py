# Aula 150 - Desafio 14 - Loop com Break e Continue
# Para este desafio, quero que você crie um loop que imprima os números de 1 a 10, mas pare de imprimir assim que chegar a 5 usando o comando "break". 
# Em seguida, crie um segundo loop que imprima os números de 1 a 10, mas pule a impressão do número 5 usando o comando "continue"

n = 1
print('Com BREAK:')
while n <= 10:
    if n == 5:
        print(n)
        break
    else:
        print(n)
        n += 1

print('Pulando o 5')
for n2 in range(1, 11):
    if n2 == 5:
        continue
    print(n2)