# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre
# 1 e 50.

#Versão da aula
for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')

#Versão 2
for n in range(2, 51, 2):
    print('.', end='')
    print(n, end=' ')
print('Acabou')
