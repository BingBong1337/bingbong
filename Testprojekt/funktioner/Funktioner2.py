import random as rand
def Slumptal(antal):
    i = 1
    while i <= antal:
        slumptal=rand.randint(1, 100)
        print(f'{slumptal}')
        i=i+1
Slumptal(5)
