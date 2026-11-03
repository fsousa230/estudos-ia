# Aula 111 - Criando o primeiro Modulo
def somar():
    print('Essa função vai somar valores')


def multi():
    print('Essa função vai multiplicar valores')



# Aula 114 - Aplicando um modulo
def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1