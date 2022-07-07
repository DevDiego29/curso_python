print('ler um número real qualquer e mostrar sua porção inteira')
#Resposta 1
'''import math
num = float(input('digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))'''

#Resposta 2
'''from math import trunc
num = float(input('digite um valor :'))
print('o valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))'''

#Resposta 3
num = float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))