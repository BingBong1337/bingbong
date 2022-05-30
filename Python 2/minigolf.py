try:
    AntalBanor = int(input('Hur många banor spelas? 2-10 st->'))
    diff = -2*AntalBanor - AntalBanor//2
    if AntalBanor > 10 or AntalBanor < 2: print('Det var inte rätt')
    for i in range(AntalBanor):
        AntalSlag = int(input('Hur många slag på bana ' +str(i+1)+ '?'))
        if AntalSlag > 7: AntalSlag = 7
        diff += AntalSlag
    print(diff)
except: print('Minigolf supportar inte flytal')