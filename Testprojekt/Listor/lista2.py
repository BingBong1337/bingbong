# Joel, Rufus och Rasmus M
# Skapar en tom lista
listan = []

# Funktion som visar hela listan
def visaLista(listan):
  print(listan)

# Funktion som lägger till ett värde i listan
def merILista(listan):
  try:
    n = float(input('Vilket värde vill du lägga till i listan? '))
  except ValueError:
      print('Ogiltigt svar')
      return
  listan.append(n)
  return listan

# Funktion som sorterar listan i storleks ordning
def sortLista(listan):
  listan.sort()
  return listan

# Funktion som visar ett valfritt värde i listan
def visaEnPosition(listan):
  try:
    n = int(input('Vilken specific listpostion vill du visa? '))
  except ValueError:
      print('Ogiltigt svar')
      return
  if n > len(listan) or n < 1:
    print('Positionen finns inte')
  else:
    print(listan[n-1])

# Funktion som tar bort ett värde i listan
def taBortILista(listan):
  if len(listan) == 0:
    print('Går inte att ta bort ett värde i listan')
  else:
    try:
      n = int(input('Vilken position i listan vill du ta bort? '))
    except ValueError:
      print('Ogiltigt svar')
      return
    del listan[n-1]
    return listan

# Funktion som beräknar listans medelvärde
def medelLista(listan):
  if len(listan) == 0:
    print('Går inte att beräkna medelvärde')
  else:
    medel = sum(listan) / len(listan)
    print(f'Medelvärdet på listan är {medel}')

# skriver ut alternativ
def val():
  print('')
  print('1. Titta på hela Listan')
  print('2. Lägg till något i Lista')
  print('3. Sortera Listan')
  print('4. Titta på en specifik List position')
  print('5. Ta bort ett värde ur Listan')
  print('6. Beräkna Listans medelvärde')
  print('7. Avsluta')
  print('')

# -------------- start av programet --------------------
svar = 0
while svar != '7':
  val()
  svar = input('Vad vill du välja? (1-7) --> ')
  print('')
  if svar == '1':
    visaLista(listan)
  elif svar == '2':
    listan = merILista(listan)
  elif svar == '3':
    listan = sortLista(listan)
  elif svar == '4':
    visaEnPosition(listan)
  elif svar == '5':
    listan = taBortILista(listan)
  elif svar == '6':
    medelLista(listan)
  elif svar == '7':
    print('Programmet är avslutat')
  else:
    print('Ogiltigt svar, försök igen')
