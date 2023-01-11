from random import randint
print('Valores sorteados:')
numero = (randint(1, 10), randint(1, 10), randint(1, 10),
randint(1, 10), randint(1, 10))
for n in numero:
    print(f'{n} ', end='')
print()
print(f'O maior valor sorteado foi: {max(numero)}')
print(f'O maior valor sorteado foi: {min(numero)}')