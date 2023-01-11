resp = 'S'
soma = 0
qtd = 0
maior = 0
menor = 0
media = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    qtd = qtd + 1
    if qtd == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / qtd
print('Você digitou {} números. A soma é {} e a média deles é {}'.format(qtd, soma, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))