import os, sys
f = open(os.path.join(sys.path[0], 'indata.in'), 'r')
input = f.read().rstrip('\n').split(" ")
import math
Ugrön = int(input[0])
Mgrön = int(input[1])
if Mgrön < 2 or Mgrön > 400000000:
    print('nej')
    exit()
if Ugrön < 0 or Ugrön > 400000000:
    print('nej')
    exit()
time = 0

if Ugrön == 0:
    time += 10*Mgrön
if Mgrön == Ugrön and Mgrön > 1 and Ugrön > 1:
    time += 10*3 #10 min för alla utan kort, 10 min för hälften av de med grönt kort och 10 min till för den sista halvan av grönt kort om de är samma fast större än 1
if Mgrön == 1:
    time += 10*Ugrön
if Mgrön < Ugrön:
    s=math.ceil(Ugrön/Mgrön)
    time += 10*s
    if Mgrön > 1:
        time += 20
    else:
        time += 0
if Mgrön > Ugrön and Ugrön != 0:
    time += 10
    if Mgrön > 1:
        time += 20
    



print(time)