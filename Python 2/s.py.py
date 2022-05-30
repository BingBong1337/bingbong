line = input()
a, b = line.split()
a = float(a)
b = float(b)
if a > b:
    print(b, a)
else:
    print(a, b)