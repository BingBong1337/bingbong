s = input('Skriv hey med godtyckligt nummer av e -->')

n = len(s)
nn = n-1


if 'e' in s:
    split = ( [char for char in s])
    split.pop(0)
    split.pop()
    NewSplit = split
    for i in range (len(NewSplit)):
        NewSplit.append('e')
    NewSplit.insert(0,'h')    
    NewSplit.append('y')
    hälsning = ''.join(NewSplit)
    print(hälsning)
    