'''Faça um program que leia um número inteiro e mostre na tela o seu sucessor e antecessor'''

#Versão da aula
n = int(input('Digite um número: '))
a = n - 1
b = n + 1
s = n + 1
print('Analisando o valor{}, seu antecessor é {} e o seu sucessor é {}'.format(n, a, s))

#Verão 2

n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, (n-1), (n+1)))