print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro')

#Resposta 1 - importando o Random (geral)
'''import random #Importar o randomizador de elementos (aleatório)
n1 = str(input('digite o nome do primeiro aluno: ')) #não é obrigatório colocar a string
n2 = str(input('digite o nome do segundo aluno: '))
n3 = str(input('digite o nome do terceiro aluno: '))
n4 = str(input('digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista) #choice = uma escolha 
print('o aluno escolhido foi {}'.format(escolhido))'''

#Resposta 2 - importando o Random e especificando

from random import choice
n1 = str(input('digite o nome do primeiro aluno: '))
n2 = str(input('digite o nome do segundo aluno: '))
n3 = str(input('digite o nome do terceiro aluno: '))
n4 = str(input('digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))