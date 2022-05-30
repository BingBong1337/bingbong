loop = 100
for a in range(loop):
    for b in range(loop): 
        for c in range(loop): 
            if 10*a + 3*b + 0.5*c == 100 and a+b+c == 100:
                print(a,b,c)