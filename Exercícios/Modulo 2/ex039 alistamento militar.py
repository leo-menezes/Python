from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
print(' ')
print('''Qual é o seu sexo?
[ 1 ] FEMININO
[ 2 ] MASCULINO''')
sexo = int(input('Digite a opção desejada.'))
while sexo == 0 or sexo > 2:
    print('Opção Inválida. Tente Novamente!')
    sexo = int(input('Digite a opção desejada.'))
if sexo == 1:
    print('Mulheres não precisam se alistar ao serviço militar obrigatório.')
else:
    print('Homens tem obrigação ao alistamento militar!')
    if idade == 18:
        print('Você tem que se alistar \033[1;33mIMEDIATAMENTE\033[m')
    elif idade < 18:
        saldo = 18 - idade
        print('Você tem apenas {} anos. \033[1;32mFaltam {} anos\033[m para o alistamento militar'.format(idade, saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    else:
        saldo = idade - 18
        print('Você deveria ter se alistado há \033[1;31m{} anos\033[m'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento deveria ter sido feito em {}'.format(ano))
