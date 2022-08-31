print('''-Ler o nome completo de uma pessoa:
-Imprimir o nome com todas as letras maiúsculas e minúsculas:
-Dizer quantas letras tem (sem considerar os espaços:
-Dizer quantas letras tem o primeiro nome:''')

nome=str(input('Digite seu nome completo: ')).strip()
separa=nome.split()
print(separa)
print('Nome em letras maiúsculas: {}'.format(nome.upper()))
print('Nome em letras minúsculas: {}'.format(nome.lower()))
print('O nome completo tem {} letras'.format(len(nome)-nome.count(' ')))
print('O primeiro nome é {} e tem {} letras.'.format(separa[0].upper(), len(separa[0])))