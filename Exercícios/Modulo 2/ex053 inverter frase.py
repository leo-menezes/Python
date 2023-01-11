print('Ler uma frase e informar se é um PALÍNDROMO (igausi de trás para frente')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um POLÍNDROMO!')
else:
    print('Essa frase NÃO É um POLÍNDROMO!')
