from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma das opções de jogadas abaixo:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
while jogador > 2:
    print('Jogada incorreta. Tente Novamente!')
    jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!')
sleep(0.7)
print('=='*15)
print('Computador escolheu {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('=='*15)
if jogador == 0:
    if computador == 0:
        print('EMPATE!!!')
    elif computador == 1:
        print('Você perdeu!! Papel ganha de Pedra.')
    elif computador == 2:
        print('Você ganhou!! Pedra ganha de Tesoura.')
elif jogador == 1:
    if computador == 0:
        print('Você ganhou!! Papel ganha de Pedra.')
    elif computador == 1:
        print('EMPATE!!!')
    elif computador == 2:
        print('Você perdeu!! Tesoura ganha de Papel.')
elif jogador == 2:
    if computador == 0:
        print('Você perdeu!! Pedra ganha de Tesoura.')
    elif computador == 1:
        print('Você ganhou!! Tesoura ganha de Papel.')
    elif jogador == 2:
        print('EMPATE!!!')

