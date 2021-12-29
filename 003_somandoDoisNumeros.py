# Crie um programa que leia dois números e mostre a soma entre eles.

# Minha versão
a = int(input('Digite um número: '))
b = int(input('Digite um número:'))
c = a + b

print('A soma de ', a, ' e ', b, ' é igual a ', c)

#Versão da aula
a = int(input('Digite um número'))
b = int(input('Digite um número'))
c = a + b

print('A soma de {} e {} é igual a{}!'.format(a, b, c))
