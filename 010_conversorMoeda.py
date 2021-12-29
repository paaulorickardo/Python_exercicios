#Crie um program de leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Doláres ela pode conseguir

#Versão da aula
real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 5.77
euro = real / 6.53
print('Com R${} você pode comprar US${:.2f} de doláres e US${:.2f} euros.'.format(real, dolar, euro))
