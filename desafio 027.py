n = str(input('digite o seu nome completo: ')).strip() #strip = retirar os espaços vazios
nome = n.split() #split = transformar a string em uma lista
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
# len(nome) = quantas posições tem o nome