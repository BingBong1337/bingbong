list = []
try:    
    Antal = int(input('Hur många tal har du?->'))
    if Antal > 5:
        print('Antal nummer var större än 5')
    else:

        for i in range(Antal):
            Tal = int(input('Vilket tal har du? ->'))
            list.append(Tal)
        list.reverse()
        for i in list:
            print(i)
except:
    print('Det var inte ett heltal')