nome = str(input('Digite o nome do Aluno: '))
n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
media = (n1 + n2) / 2
print('Primeira nota foi {:.2f} e a segunda nota foi {:.2f}. A média é {:.2f}.'.format(n1, n2, media))
if media < 5:
    print('O aluno {} está REPROVADO!!!'.format(nome))
elif media >= 5 and media < 7:
    print('O aluno {} está em RECUPERAÇÃO!!!'.format(nome))
else:
    print('O aluno {} está APROVADO. PARABÉNS!!!'.format(nome))