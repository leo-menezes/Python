from random import randint
v = 0
while True:
    jogador = int(input('Informe um número para jogar: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer PAR ou ÍMPAR? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total = {total}')
    print('Deu PAR. ' if total % 2 == 0 else 'Deu ÍMPAR. ', end='')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ GANHOU!!!')
            v = v + 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ GANHOU!!!')
            v = v + 1
        else:
            print('VOCÊ PERDEU!!!')
            break
        print('Jogue novamente...')
print(f'FIM...Você venceu {v} vezes...')