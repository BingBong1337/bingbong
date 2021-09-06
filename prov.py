import os

os.system('cls')

resultat = []
try:
    elever = int(input('hur många elever befinner sig i rummet?-->'))
    for i in range (elever):
        provresultat = input('skriv in provresultatet--> ')
        resultat.append(provresultat)
    print(resultat)
except:
    print('nej, försök igen')
