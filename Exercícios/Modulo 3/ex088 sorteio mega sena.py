from random import randint
from time import sleep
lista = []
jogos = []
print('Jogos para Mega Sena')
print()
quant = int(input('Quantos jogos você quer? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total = total + 1
print('   SORTEANDO   ')
print(f'Os números sorteados foram:')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('*** BOA SORTE! ***')
