peso = float(input('Digite o seu peso: (kg)'))
altura = float(input('Digite a altura: (m)'))
imc = peso / (altura ** 2)
print('Seu Índice de Massa Corpórea (IMC) é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Seu peso está ideal!')
elif imc > 25 and imc <= 30:
    print('Você está em sobrepeso!')
elif imc > 30 and imc <= 40:
    print('Você está OBESO. Atenção!!!')
else:
    print('CUIDADO! Você está com OBESIDADE MÓRBIDA!!!')