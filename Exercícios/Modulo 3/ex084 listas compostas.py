'''leia nome e peso de várias pessoas
 guardando tudo em uma lista.
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
pessoas = []
grupo = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso (Kg): ')))
    if len(grupo) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    grupo.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer continuar? (S/N): '))
    if resp in 'Nn':
        break
print(f'Total de pessoas cadastradas: {len(grupo)}')
print(grupo)
print(f'maior peso: {maior}kg', end='')
for p in grupo:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'menor peso: {menor}kg', end='')
for p in grupo:
    if p[1] == menor:
        print(f'[{p[0]}]')

