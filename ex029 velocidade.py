print('Digitar a velocidade do carro. Se exceder 80km, pagará uma multa de R$ 7,00 por km excedido')
print(' ')
print('DIRIJA COM SEGURANÇA')
velocidade = float(input('Qual a velocidade que o carro estava na pista? '))
if velocidade >80:
    print('Você passou a {}KM/H e a velocidade permitida que é de 80KM/H'.format(velocidade))
    multa = (velocidade-80) * 7
    print('o valor da multa é de R${:.2}'.format(multa))
else:
    print('Parabéns! Continue dirigindo com segurança')