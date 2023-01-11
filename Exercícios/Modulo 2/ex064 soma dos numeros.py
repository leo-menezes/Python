num = 0
cont = 0
soma = 0
num = int(input('Digite um número. Se quiser parar, digite (999): '))
while num != 999:
    cont = cont + 1
    soma = soma + 1
    num = int(input('Digite um número. Se quiser parar, digite (999): '))
print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))
