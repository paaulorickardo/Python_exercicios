# Desenvolva um programa que leia o primeiro termo e a razao de uma PA
# No final, mostre os 10 primeiros termos dessa progressão

#Versão da aula

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end=' ')
print('ACABOU!')