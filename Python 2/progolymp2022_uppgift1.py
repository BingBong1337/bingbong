area_C4 = 0.229*0.324
area_A3 = 0.297*0.42
area_A4 = 0.21*0.297
vikt_kuvert = int(input('Kuvert vikt->'))
vikt_affisch = int(input('Affisch vikt->'))
vikt_blad = int(input('Blad vikt->'))
if vikt_kuvert < 50 or vikt_kuvert > 200 or vikt_affisch < 50 or vikt_affisch > 200 or vikt_blad < 50 or vikt_blad > 200:
    print('inte ok')
    exit()
else:
    areavikt_kuvert = vikt_kuvert*area_C4
    areavikt_affisch = vikt_affisch*area_A3
    areavikt_blad = vikt_blad*area_A4

total_vikt = areavikt_kuvert*2+areavikt_blad+areavikt_affisch*2
vikt = '{:.6f}'.format(total_vikt)
print('brevet väger',vikt,'gram')