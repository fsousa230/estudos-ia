# Aula 112 - Importando um Modulo
'''import secao15_funcoes

secao15_funcoes.somar()
secao15_funcoes.multi()

# ou da seguinte forma

from secao15_funcoes import somar, multi

somar()
multi()'''

# Aula 113 - Importando Package
'''from secao15_funcoes import somar, multi
from secao15_items.cadastro import cliente

somar()
multi()
cliente()'''

# Aula 114 - Aplicando um modulo
from secao15_funcoes import find_index

list1 = ['a', 'b', 'c', 'd', 'e']

var1 = find_index(list1, 'g')
print(var1)