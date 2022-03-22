# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressao usando a estrutura
# while

#Versão da aula

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Razão da PA: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')