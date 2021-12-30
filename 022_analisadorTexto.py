'''Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas e minúsculas, qtd letras ao todo (
sem espaço) qtas letras tem o primeiro nome'''

#versão aula
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem{} letras'.format(nome.find(' '))
#versao dois
separa = nome.split() #separa os nomes em uma lista sem pegar os espaços
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


