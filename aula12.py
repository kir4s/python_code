preço = float(input('qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('o produto que custava R${:.2f}, na promoçâo com desconto de 5% vai custar R${:.2f}'.format(preço,  novo))


# Para calcular % colocamos o preço X (o valor da % que deseja calcular) dividido por 100