lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#for c in lanche:
#   print(f'Eu vou comer {c}')

#for cont in range(0, len(lanche)):
#    print(lanche(cont))

for pos, comida in enumerate(lanche):
    print(f'O nº{pos} no cardápio é {comida}')