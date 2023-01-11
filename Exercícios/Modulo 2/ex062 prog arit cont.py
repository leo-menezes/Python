primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('Pronto...')
    mais = int(input('Quantos números quer ver a mais?'))
print('FIM...{} termos foram mostrados'.format(total))