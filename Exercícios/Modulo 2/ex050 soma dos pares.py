soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Insira o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Foi/Foram inserido(s) {} número(s) pares e a soma dele(s) é {}'.format(cont, soma))
