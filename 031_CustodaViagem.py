# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule
# o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$ 0,45
# para viagens mais longas.

#Versão 01 aula

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('É o preço da sua passagem será de R${:.2f}'.format(preço))

#Versão dois com operador ternário

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('É o preço da sua passagem será de R${:.2f}'.format(preço))

