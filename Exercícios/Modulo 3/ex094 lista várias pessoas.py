pessoa = {}
galera = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print()
print(f'Total de pessoas cadastradas: {len(galera)}')
media = soma / len(galera)
print(f'Média de idade das pessoas cadastradas: {media:5.2f}')
print('Mulheres cadastradas: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Pessoas com idade acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('fim...')