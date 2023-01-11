while True:
    n = int(input('Insira um número para ver a tabuada correspondente: '))
    print('-'*20)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x{c} = {n * c}')
    print('-' * 20)
    print('')
print('PROGRAMA ENCERRADO')