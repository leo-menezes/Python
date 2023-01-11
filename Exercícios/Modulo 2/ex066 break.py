soma = 0
qtd = 0
while True:
    n = int(input('Digite um número. [999] p/ parar: '))
    if n == 999:
        break
    soma = soma + n
    qtd = qtd + 1
print(f'Você digitou {qtd} números e a soma entre eles é {soma}')