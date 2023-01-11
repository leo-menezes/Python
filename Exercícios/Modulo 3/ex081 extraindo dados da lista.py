'''Ler vários números e colocar em uma lista, informando:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'Fora digitados {len(lista)} números para a lista: {lista}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica: {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista')
else:
    print('O número 5 NÃo faz parte da lista')