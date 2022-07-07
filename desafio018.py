print('ler um ângulo qualquer, o valor do seno, cosseno e a tangente desse ângulo')

#Resposta 1 - importando o math (geral)
'''import math
ângulo = float(input('digite o valor do ângulo: '))
seno = math.sin(math.radians(ângulo)) #converter em radianos e mostrar o valor do seno
print('O ângulo {} terá o SENO {}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo {} terá o COSSENO {}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo {} terá a TANGENTE {}'.format(ângulo, tangente))'''

#Resposta 2 - especificando a importação

from math import radians, sin, cos, tan
ângulo = float(input('digite o valor do ângulo: '))
seno = sin(radians(ângulo)) #converter em radianos e mostrar o valor do seno
print('O ângulo {} terá o SENO {}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo {} terá o COSSENO {}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo {} terá a TANGENTE {}'.format(ângulo, tangente))
