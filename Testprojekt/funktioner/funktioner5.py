import math
def diameter(d):
    r=d/2
    a=r*r*math.pi
    return a
area = diameter(int(input('vad är d ->')))
print(f'{area}')
