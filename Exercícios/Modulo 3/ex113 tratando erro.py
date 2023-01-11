def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Favor digitar um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário...')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Favor digitar um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário...')
            return 0
        else:
            return n


num = leiaint('Digite um valor: ')
num2 = leiafloat('Digite um valor com casas decimais: ')
print(f'O valor digitado foi {num}')
print(f'O valor digitado foi {num2}')