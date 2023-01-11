print('Digite um número e diga qual é o maior valor ou se são iguais...')
n1 = float(input('Primeiro Número: '))
n2 = float(input('Segundo Número: '))
if n1 > n2:
    print('O \033[7mPRIMEIRO\033[m valor é maior!')
elif n1 < n2:
    print('O \033[7mSEGUNDO\033[m valor é maior!')
else:
    print('Os dois números são \033[7mIGUAIS\033[m!')
