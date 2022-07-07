salário = float(input('qual é o salário do funcionário: R$'))
novo = salário + (salário * 15 / 100)
print('um funcionário que ganhava R${:.2F}, com 15% de aumento, passa a ganhar R${:.2f}'.format(salário, novo))