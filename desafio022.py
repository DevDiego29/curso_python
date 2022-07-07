print('lendo o nome completo de uma pessoa')
nome = str(input('digite o seu nome completo: '))
print('analisando seu nome...')
print('seu nome em maiúsculo é {}'.format(nome.upper()))
print('seu nome em minúsculo é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#len(nome) = ler a quantidade de caracteres #nome.count(' ') = não contar o espaço vazio entre os nomes
#Resposta 1
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
#nome.find(' ') = o espaço vazio se encontra em qual posição, retornando nesse caso posição 5
#Resposta 2
separa = nome.split() #split = joga em uma lista 
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))