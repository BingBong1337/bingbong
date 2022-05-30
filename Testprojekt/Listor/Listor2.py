minLista = []
print('1. Titta på hela Listan')
print('2. Lägg till något i Lista')
print('3. Sortera Listan')
print('4. Titta på en specifik List position')
print('5. Ta bort ett värde ur Listan')
print('6. Beräkna Listans medelvärde')
print('7. Avsluta')
VadVillDuGöra = int(input())
def main():
    VadVillDuGöra = ''


    while VadVillDuGöra != 7:
    VadVillDuGöra = int(input('Vad vill du göra? -->'))

if VadVillDuGöra==1:
    print(minLista)
elif VadVillDuGöra==2:
    minLista.append(int(input('vad vill du lägga till?')))
elif VadVillDuGöra==3:
    print(sorted(minLista))
elif VadVillDuGöra==4:
    k=int(input('ListPlats?-->'))
    print(minLista[f'{k}'])
