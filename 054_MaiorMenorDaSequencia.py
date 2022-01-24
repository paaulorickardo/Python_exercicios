# Faça um programa que leia o peso de cinco pessoas.No final, mostre qual
# foi a maior e o menor peso lidos.

#Versão da aula

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))


#Minha versão
totmaior = 0
totmenor = 0
for pess in range(1,6):
    peso = float(input('Peso da {}ª :'.format(pess)))
    if peso > pess:
        print('O maior peso lido foi de  {} kg'.format(peso))
    else:
        print('O menor peso lido foi de  {} kg '.format(peso))




