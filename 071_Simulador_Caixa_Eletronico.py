# Crie um programa que simule o funcionamento de um cx eletronico. No incio,
# pergunte ao usuário qual será o valor a ser sacado(numero inteiro) e o programa
# vai informar qtas cédulas de cada valor serão entregues

#Versão da aula
print('=' * 30)
print('{:^30}'.format('BANCO DEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO DEV! Tenha um bom dia!')