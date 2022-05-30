prisGuldsmycke = 1000
prisSilversmycke = 500
prisJärnsmycke = 200
fattig = 0
Pengar = int(input('Hur mycket pengar har du kompis? ->'))
if Pengar >= prisGuldsmycke:
    print('Du kan köpa ett Guldsmycke polarn')
elif Pengar >= prisSilversmycke:
    print('Du kan köpe silver mannen')
elif Pengar >= prisJärnsmycke:
    print('Du kan köpa järn killen')
elif Pengar >= fattig:
    print('pank')
if Pengar <= fattig:
    print('REEEEEEEEEEEEEEEEEEEEEEEEEEE')
