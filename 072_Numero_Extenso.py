# Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de zero
# até vinte.
#
# Seu programa deverá ter um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <=20:
        break
    resp =' '
    while resp not in 'SN':
        resp = str(input('Tente Novamente.Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você digitou o número {cont[num]}')


