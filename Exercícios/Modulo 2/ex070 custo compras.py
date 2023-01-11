total = 0
tot1000 = 0
menor = 0
cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Valor do produto: R$ '))
    cont = cont + 1
    total = total + preco
    if preco > 1000:
        tot1000 = tot1000 + 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if menor < menor:
            menor = preco
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de: R$ {total}')
print(f'Produtos acima de R$ 1.000,00 : {tot1000}')
print(f'O produto mais barato foi {barato} e custou R$ {menor}')