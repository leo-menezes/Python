'''from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

n = int(input('Digite um número para saber seu fatorial:'))
c = n
f = 1
print('O fatorial de {} é: '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))