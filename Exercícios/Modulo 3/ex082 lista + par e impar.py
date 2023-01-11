'''Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
lista.sort()
print(f'Os números incluídos na lista foram: {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
par.sort()
impar.sort()
print(f'A lista dos números pares é: {par}')
print(f'A lista dos números ímpares é: {impar}')