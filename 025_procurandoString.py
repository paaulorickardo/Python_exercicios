#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

#Versão da aula
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Barbosa? {}'.format('barbosa' in nome.lower()))
