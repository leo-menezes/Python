#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço normal
#– 3x ou mais no cartão: 20% de juros

produto = str(input('Indique qual produto você deseja comprar: ')).upper()
valor = float(input('Digite o valor do produto: R$'))
print('''Escolha a forma de pagamento abaixo:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais, no cartão de crédito''')
forma = int(input('Digite a opção desejada: '))
if forma == 1:
    preco = valor - (valor * 0.1)
    print('O Produto {} sai à R${:.2f}'.format(produto, preco))
elif forma == 2:
    preco = valor - (valor * 0.05)
    print('O produto {} sai à R${:.2f}'.format(produto, preco))
elif forma == 3:
    parcela = valor / 2
    print('O produto {} sai à R${:.2f}'.format(produto, valor))
    print('Cada parcela sai no valor de R${:.2f}'.format(parcela))
elif forma == 4:
    prestacao = int(input('Informe o número de parcelas para pagamento: '))
    if prestacao >= 3:
        preco = valor + (valor * 0.2)
        parcela = preco / prestacao
        print('O produto {} sai pelo valor de R${:.2f}'.format(produto, preco))
        print('O pagamento será em {} parcelas de R${:.2f}'.format(prestacao, parcela))
    else:
        print('Quantidade de parcelas inválidas para essa forma de pagamento')
else:
    print('Opção Inválida. Tente Novamente')