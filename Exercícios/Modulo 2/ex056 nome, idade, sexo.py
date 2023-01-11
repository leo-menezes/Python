somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range (1,5):
    print('{}ª pessoa'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher = totmulher + 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho é o {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('No grupo tem {} mulheres com menos de 20 anos'.format(totmulher))
