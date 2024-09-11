km = int(input('Digite quantos km será sua viagem: '))
if km <= 200:
    a = km * 0.50 
    print('Sua viagem custará R${} '.format(a))
else:
    a = km * 0.45
    print('Sua viagem custará R${} '.format(a))