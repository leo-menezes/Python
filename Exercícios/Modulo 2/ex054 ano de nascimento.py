from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoas in range(1, 8):
    ano = int(input('Digite o ano que a {}ª pessoa nasceu'.format(pessoas)))
    idade = atual - ano
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor +1
print('Da lista, {} pessoas são maiores de idade'.format(maior))
print('Da lista, {} pessoas são menores de idade'.format(menor))