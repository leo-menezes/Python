idade18 = 0
idademenor = 0
totmasc = 0
totfem = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade < 18:
        idademenor = idademenor + 1
    if idade >= 18:
        idade18 = idade18 + 1
    if sexo == 'M':
        totmasc = totmasc + 1
    if sexo == 'F':
        totfem = totfem + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*30)
print(f'Pessoas com menos de 18 anos: {idademenor}')
print(f'pessoas com mais de 18 anos: {idade18}')
print(f'Total de homens: {totmasc}')
print(f'Total de mulheres: {totfem}')