print('''Reajuste de salário:
10% para salário acima de R$ 1250,00
15% para salários menores ou iguais a R$ 1250,00''')
print(' ')
salario = float(input('Digite o valor do salário atual: R$'))
if salario > 1250:
    reajuste = salario * 0.1
else:
    reajuste = salario * 0.15
ns = salario + reajuste
print('O salário de {:.2f}, terá um reajuste de {:.2f} e passa a ser de \033[7m{:.2f}\033[m'.format(salario, reajuste, ns))
