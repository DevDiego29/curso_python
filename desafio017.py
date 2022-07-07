print('comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo')
#Resposta 1 - sem importar
'''co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2)** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

#Resposta 2 - importando o math (geral)
'''import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

#Resposta 3 - importando o hypot (especificando)
from math import hypot
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))