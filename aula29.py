print('Bem vindo ao detran')


km = int(input('Quantos km você estava na hora da multa?: ')) 
if km <= 80:
    print('Essa multa foi um erro, você esta liberado!')
else:
    km = (km - 80) * 7
    print('sua multa deu {}!'.format(km))

