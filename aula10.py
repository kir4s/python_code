real = float(input('Quanto dinheiro você tem na carteira? R$'))
# cotaçao
cotacao_dolar = 5.63
cotacao_euro = 6.17
# Cálculo
dolar = real / cotacao_dolar
euro = real / cotacao_euro
#saida
print('com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('com R${:.2f} voce pode comprar EUR{:.2f}'.format(real, euro))
# comando ":.2f" pra ter duas casas decimais flutuantes