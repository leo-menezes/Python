from datetime import date
atual = date.today().year
nome = str(input('Digite o nome do atleta: '))
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
print('O atleta {} tem {} anos.'.format(nome, idade))
if idade <= 9:
    print('Este atleta é da categoria MIRIM')
elif idade <= 14:
    print('Este atleta é da categoria INFANTIL')
elif idade <= 19:
    print('Este atleta é da categoria JÚNIOR')
elif idade <= 25:
    print('Este atleta é da categoria SÊNIOR')
else:
    print('Este atleta é da categoria MASTER')