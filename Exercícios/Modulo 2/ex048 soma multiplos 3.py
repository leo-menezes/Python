cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('Existem {} números ímpares que são divisíveis por 3'.format(cont))
print('A soma de todos os valores dá {}'.format(soma))