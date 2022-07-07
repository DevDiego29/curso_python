print('ler um número de 0 a 9999 e mostrar cada um dos dígitos separados')

num = int(input('digite um valor: '))
u = num // 1 % 10 #Divisão inteira por 1 e o resultado eu tiro o módulo, ou seja, o resto da divisão por 10
d = num // 10 % 10 #Divisão inteira por 10 e o resultado eu tiro o resto da divisão por 10
c = num // 100 % 10 #Divisão inteira por 100 e o resultado eu tiro o resto da divisão por 10
m = num // 1000 % 10 #Divisão inteira por 1000 e o resultado eu tiro o resto da divisão por 10
print('analisando o número {}'.format(num))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))