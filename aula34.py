salario = float(input('Digite o salario do funcionario? R$: '))
if salario <= 1250:
    #salario *15 /100 pra saber a % 
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario *10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora .'.format(salario, novo))