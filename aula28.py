from random import randint
from time import sleep #funçao sleep faz o pc dormir e ter um atraso na linha de codigo
computador = randint(0, 5)
print('--' * 20)
print('Vou pensar em um numero entre 0-5. Tente adivinhar...')
print('--' * 20)
jogador = int(input('Em que número eu pensei?: '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('Eu pensei no numero {} nâo no numero {}!'.format(computador, jogador))