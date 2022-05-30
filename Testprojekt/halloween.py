import random as r
AntalGrannar = 10
Godis = [0]
def merGodis():
    merGodis = Godis.append(+2)
    print(f'Du fick godis!!! Du har nu {sum(Godis)} godis')
    return
def ingeGodis():
    ingeGodis = Godis.append(-1)
    print(f' Danskjävlarna tog godis ifrån dig, du har nu {sum(Godis)} godis')
    return
def horGranne():
    horGranne = Godis.append(-5)
    print(f'Du gick till horgrannen som tog 5 st godisar ifrån dig, du har nu {sum(Godis)} godis.')
    return
def coolGranne():
    coolGranne = Godis.append(+5)
    print(f'Du knacka på hos den coola grannen som gav dig mycket godis, du har nu {sum(Godis)} godis.')
def inteBra():
    inteBra = Godis.append(-sum(Godis))
    print(f'Inte bra du tappade all ditt godis, du har nu {sum(Godis)} godis.')
for i in range(AntalGrannar):
    Hus = r.randint(0,10)
    if Hus > 3:
        merGodis()
    elif Hus == 1:
        horGranne()
    elif Hus == 2:
        coolGranne()
    elif Hus == 3:
        inteBra()
    else:
        ingeGodis()

print(f'Du fick sammanlagt {sum(Godis)} godis ')
