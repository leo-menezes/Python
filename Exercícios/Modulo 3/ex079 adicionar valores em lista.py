'''Cadastrar valores em lista, eliminando os repetidos. colocar em ordem crescente'''

numeros = []
while True:
    n = int(input('Digite um número para adicionar na lista: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Número inserido anteriormente. Não será adiconado na lista.')
    resposta = str(input('Quer continuar adicionando? [S/N]: '))
    if resposta in 'Nn':
        break
print()
numeros.sort()
print(f'Você inseriu os números {numeros}')