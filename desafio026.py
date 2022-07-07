frase = str(input('digite uma frase: ')).upper().strip()#upper = deixar tudo em maiúsculo #strip = retirar os espaços
print('a letra A aparece {} vezes na frase'.format(frase.count('A'))) #frase.count = contar quantas vezes aparece o 'A'
print('a primeira letra A aparece na posição {}'.format(frase.find('A')+1)) #find = em que posição aparece o 'A'
print('a ultima letra A aparece na posição {}'.format(frase.rfind('A')+1)) #rfind = em que posição na direta aparece 'A'