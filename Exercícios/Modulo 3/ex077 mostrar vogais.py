'''Pegar as vogais de cada palavra da lista e informar'''

palavras = ('Jogador', 'Atleta', 'Passeio', 'Solucionar',
            'Leandro', 'Nome', 'Portugal', 'Brasil',
            'Filho', 'Criança')
for p in palavras:
    print(f'\n{p.lower()} contém as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')