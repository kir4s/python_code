import random 


print('Bem vindo, nesse mini game irei pensar em um numero de 1-5, boa sorte pra acertar')
numero_aleatorio = random.randint(1,5)
a = int(input('digite um numero: '))
if a == numero_aleatorio:
    print('Parabens você acertou!')
else:
    print('você errou!')
    print('--GAME-OVER--')

