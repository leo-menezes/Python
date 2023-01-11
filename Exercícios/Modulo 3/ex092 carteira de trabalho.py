from datetime import date
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Digite o ano de nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Informe o nº da carteira de trabalho: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano da primeira contratação: '))
    dados['salário'] = float(input('Informe o valor do primeiro salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
print()
for k, v, in dados.items():
    print(f'{k}: {v}')
