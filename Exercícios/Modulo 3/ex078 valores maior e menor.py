'''Digitar valores para uma lista e informar o maior e o menor e suas posições'''

num = []
maior = 0
menor = 0
for n in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n == 0:
        maior = menor = num[n]
    else:
        if num[n] > maior:
            maior = num[n]
        if num[n] < menor:
            menor = num[n]

print(f'Os valores digitados foram {num}')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')

