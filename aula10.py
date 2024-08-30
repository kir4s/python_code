real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real /5.63
print('com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
# comando ":.2f" pra ter duas casas decimais flutuantes 
