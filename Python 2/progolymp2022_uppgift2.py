import os, sys
f = open(os.path.join(sys.path[0], 'indata.in'), 'r')
input = f.read().rstrip('\n').split(" ")

mening_längd = int(input[0])
print('hur många ord i meningen?->', mening_längd)

vokaler = ['a','e','i','o','u','y']

mening = ''
for i in range(mening_längd):
    mening += ' '
    mening += input[i+1]

for i in range(len(mening)):
    if (len(mening) - i > 2):
        if any(k in mening[i] for k in vokaler) == True:
            if (any(k in mening[i+1] for k in vokaler) == False) and (any(k in mening[i+2] for k in vokaler) == False) and (mening[i+1] != " ") and (mening[i+2] != " "):
                mening = mening[:i] + mening[i+1:]

arabic_mening = mening[::-1]
print(arabic_mening)