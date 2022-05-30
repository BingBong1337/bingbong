import random
alphabet = tuple('abcdefghijklmnopqrstuvwxyz')

print('\n' .join(repr(u)) for u in globals() if not u.startswith('__'))

for i in range(8):
    globals()[''.join(random.sample(alphabet,random.randint(3,26)))] = random.choice(alphabet)



print ('\n'.join(repr((u,globals()[u]))) for u in globals() if not u.startswith('__'))
