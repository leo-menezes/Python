#import math
from math import hypot
co=float(input('Digite o valor do Cateto Oposto: '))
ca=float(input('Digite o valor do Cateto Adjacente: '))
hi=hypot(co,ca)
print('A Hipotenusa mede {:.2f}'.format(hi))