print('Digite a distância do local de partida para o destino pretendido, para calcularmos a viagem.')
destino=float(input('Digite a distância em KM: '))
if destino <=200:
    preco=destino*0.5
else:
    preco=destino*0.45
print('O valor da viagem é: R${:.2f}'.format(preco))