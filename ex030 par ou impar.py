print('Digite um número para saber se é PAR ou ÍMPAR')
numero=int(input('Digite o número pretendido: '))
resultado=numero%2
if resultado==0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))