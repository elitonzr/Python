lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(len(lanche))
print(lanche.count('Suco'))
print(lanche.index('Pudim'))
print('')
for i in lanche:
    print(f'Eu vou comer {i}')

print('')
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')

print('')
for pos, item in enumerate(lanche):
    print(f'Eu vou comer {item} na posição {pos}')

print('')
for s in range(0, len(lanche)):
    print(f'Eu vou comer {sorted(lanche)[s]}')
