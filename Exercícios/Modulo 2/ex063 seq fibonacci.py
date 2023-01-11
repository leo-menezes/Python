print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
n = int(input('Quantos termos da sequência você quer mostrar? '))
t1 = 0
t2 = 1
print('{} - {} - '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{}'.format(t3), end='')
    print(' - ' if cont < n else '', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('')
print('FIM...')