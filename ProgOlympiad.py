import os
import math
os.system('cls')

sum = 0
n = 1
for i in range(1000000):
    ekv = 1/n
    sum += ekv
    n+=2
    ekv = 1/n
    sum -= ekv
    n+=2
    
print(sum*4)
print(math.pi)