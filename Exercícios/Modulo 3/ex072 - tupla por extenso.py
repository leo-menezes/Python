cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente Novamente!! ', end='')
print(f'Você digitou o número {cont[num]}')
resp = ' '
while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        print('FIM...')

print('Até breve')