from random import randint
computador = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Tente advinhar o número pensado')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpite = palpite + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente!')
        elif jogador > computador:
            print('Menos...Tente novamente!')
print('Você acertou com {} tentativas!!!'.format(palpite))
