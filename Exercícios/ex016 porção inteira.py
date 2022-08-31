# import math
from math import trunc
print('Digitar um número real na tela, para mostrar a parte inteira')
num = float(input('Digite um número: '))
print('O número digitado é {} e a sua porção inteira é {}'.format(num, trunc(num)))