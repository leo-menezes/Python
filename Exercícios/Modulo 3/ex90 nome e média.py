aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'A média do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print()
for k, v in aluno.items():
    print(f'{k}: {v}')