from time import sleep
n1 = float(input('Insira o primeiro valor: '))
n2 = float(input('Insira o segundo valor: '))
opcao = 0
while opcao != 5:
    print('O que deseja fazer com os valores inseridos?')
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] SABER QUEM É O MAIOR
    [ 4 ] INSERIR NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('A soma de {} + {} é = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação de {} x {} é {:.2f}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior número é {}'.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o maior número é {}'.format(n1, n2, maior))
        else:
            print('Os números são iguais')
    elif opcao == 4:
        print('---Informe os novos valores.---')
        n1 = float(input('Insira o primeiro valor: '))
        n2 = float(input('Insira o segundo valor: '))
    elif opcao == 5:
        print('FINALIZANDO...')
        sleep(2)
    else:
        print('Opção Inválida!!!')
    print('')
print('FIM...')