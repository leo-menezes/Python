print('Digite um número e escolha a base de conversão: Binário, octal ou hexadecimal')
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO:
[ 2 ] Converter para OCTAL:
[ 3 ] Converter para HEXADECIMAL:''')
opção = int(input('Digite a opção desejada: '))
if opção == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida. Tente novamente!!!')