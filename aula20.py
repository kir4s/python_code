from random import shuffle
n1 = str(input('primeiro cliente: '))
n2 = str(input('segundo cliente: '))
n3 = str(input('terceiro cliente: '))
n4 = str(input('quarto cliente: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('a ordem de entre sorteada foi ')
print(lista)
# Nesse exerc usamos a funçao shuffle que ta dentro da bliblioteca "random" pra sortear uma ordem 