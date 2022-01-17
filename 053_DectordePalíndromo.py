# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
# ( a frase não muda de trás para frente) desconsiderando os espaços

#Versão da aula

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
'''for letra in range(len(junto) -1, -1, -1): #1 letra volta uma letra
    inverso += junto[letra]'''
#Forma mais simples
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
