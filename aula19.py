import random
n1 = str(input('primeiro cliente: '))
n2 = str(input('segundo cliente: '))
n3 = str(input('terceiro  cliente: '))
n4 = str (input('quarto cliente: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))