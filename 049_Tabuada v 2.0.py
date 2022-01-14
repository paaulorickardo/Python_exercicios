# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher
# só que agora ultilizando um laço for.


#Versão da aula

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num, c, num*c))
