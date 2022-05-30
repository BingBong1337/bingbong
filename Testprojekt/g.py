# ------------------------------- Information --------------------------------- #
"""
Titel: Bussen
Författare:
Datum:
Det här är ett program för hantering av passagerare på en buss. Programmet
lagrar passagerare i en lista.
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as r
import operator as op

# ---------------------------- Klassdefinitioner ------------------------------ #
class Person():
    """ Person är en klass för att representera personer i bussen. Varje objekt
    som skapas ur klassen har ett namn och en ålder, samt metoder för att returnera
    alternativt modifiera respektive attribut. """
    def __init__(self, namn, ålder, kön):
        self.namn = namn
        self.ålder = ålder
        self.kön = kön


    def __repr__(self):
        return '({},{},{})'. format(self.namn, self.ålder, self.kön)


    # Strängrepresentation av objektet.
    #def __str__(self):
    #    return f'Det här är {self.namn}. Hen är {self.ålder} år gammal och är {self.kön}.'
    # Setters
    def setNamn(self, nyttNamn):
        self.namn = nyttNamn

    def setÅlder(self, nyÅlder):
        self.ålder = nyÅlder

    def setKön(self, nyKön):
        self.kön = nyKön

    # Getters
    def getNamn(self):
        return self.namn

    def getÅlder(self):
        return self.ålder

    def kön(self):
        return self.kön
passagerare = []
gamal = []
aPerson = Person('','','')
bye = [1,2,3,4,5,6,7,8,9,10,'q']
namnLista=['Love', 'Ashley', 'Charlie', 'Kim', 'Billie', 'Noa', 'Nico','Mika','Lee',
'Michele','Valentin','Minou','Lo','Cleo','Boobie', 'Robin', 'Jordan', 'Ziggy','Elliot','Eli','Dani','Taylor','Mango','Pixi','Filur']
buss = []
def buss_sortÅlder(aPerson):
    return aPerson.ålder
def buss_sortNamn(aPerson):
    return aPerson.namn



# ------------------------- Funktionsdefinitioner ---------------------------- #
 # Gör en lista men alla personer
def namn():
    aPerson.namn = namnLista[(r.randint(0,24))]
    return
def år():
    aPerson.ålder = r.randint(0,100)
    gamal.append(aPerson.ålder)
    return

def kön():
    kön = r.randint(1,3)
    if kön == 1:
      aPerson.kön = ('han')
    elif kön == 2:
      aPerson.kön = ('hon')
    elif kön == 3:
      aPerson.kön = ('hen')
      return


# Lägger till en ny person i bussen.
def plockaUpp():
    if sum(passagerare) >= 25:
        print('Fullt på bussen')
    else:
        namn()
        år()
        kön()
        buss.append(aPerson)
        print(buss)

        #buss.append(f'aPerson{namn,år,kön}')
        #buss.append(Person(namn,år,kön))
        passagerare.append(+1)
        print(f'Du plocka upp {aPerson.namn}, {aPerson.kön} är {aPerson.ålder} år gammal, du har nu {sum(passagerare)} passagerare')
        return

    return




# Avlägsnar en person från bussen.
def gåAv():
    if sum(passagerare) == 0:
        print('Du har inga passagerare så du kan inte släppa av någon')

    else:
        passagerare.append(-1)
        print(f'Du släppte av {buss[0:1]}, Du har nu {sum(passagerare)} passagerare')
        buss.pop(0)
        gamal.pop(0)
        return

# Listar alla passagerare på bussen.
def skrivUt():
        if len(buss) == 0:
            print('Ingen på bussen')
        else:
            #print(f'Din buss kör {buss} ' )
            for namn in buss:
                print(f'Din buss kör {namn}')
            return

# Skriver ut den sammanlagda åldern på passagerarna.
def sammanlagdÅlder():
    if len(buss) == 0:
        print('Ingen på bussen att beräkna medelåldern på')
    else:
        try:
            print('Summan av alla åldrar på bussen är',sum(gamal))
        except:
            print('Finns ingen på bussen att beräkna medelåldern på')
    return

# Skriver ut medelåldern på passagerarna i bussen.
def medelÅlder():
    try:
        print('Medelåldern på bussen är',sum(gamal)/len(gamal))
    except:
        print('Finns ingen på bussen att beräkna medelåldern på')
    return


# Skriver ut personen som är äldst på bussen.
def äldst():
    namn = 1
    if namn == 1:

        print('Äldst:\n', sorted(buss, key = buss_sortÅlder, reverse=True))

        return

# Sorterar bussen, antingen efter namn i bokstavsordning eller efter ålder.
def busSort():
    if len(buss) == 0:
        print('Det finns ingen att sortera på bussen')
    else:
        try:
            n = input('Vill du sortera bussen efter namn(n) eller ålder(å)?-->')
            if n != 'n' and n != 'å':
                print('Förlåt, jag förstod inte försök igen')
            else:
                if n == 'n':
                    s = int(input('Bokstavsårdning A-Ö(1) eller Ö-A(2) -->'))
                    if s != 1 and s != 2:
                        print('Kan du ta om det?')
                    if s == 1:
                        print(sorted(buss, key = buss_sortNamn))
                    elif s == 2:
                        print(sorted(buss, key = buss_sortNamn, reverse = True))
                elif n == 'å':
                    d = int(input('Äldst eller yngst?(1 för äldst... 2 för yngst)'))
                    if d != 1 and d != 2:
                        print('Kan du ta om det?')
                    if d == 1:
                        print(sorted(buss, key = buss_sortÅlder))
                    elif d == 2:
                        print(sorted(buss, key = buss_sortÅlder, reverse = True))

        except:
            print('Fel, försök igen!')
            return




# Skriver ut en lista på alla passagerare inom ett visst åldersspann.
def hittaPassagerare():
        try:
            s = int(input("Vad är maxåldern för ålderspannet?"))
            n = int(input("Vad är minimumåldern för ålderspannet?"))
            for n in range(n, s+1):
                for aPerson in buss:
                    if aPerson.ålder == n:
                        print(f'Passageraren {aPerson.namn} är {aPerson.ålder} år gammal')

        except:
            print("Det du valde var inte ett giltigt alternativ, vänligen försök igen")

        return

# petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta(passagerare):
    return

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    menyVal = ""


    while menyVal != "q":
        print(
        """
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                        2. Låt passagerare gå av
            3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
            5. Beräkna medelåldern                              6. Hitta äldst person
            7. Sortera bussen                                   8. Hitta personer inom ett specifikt åldersspann
            9. Peta på passagerare                              q. Avsluta
        ---------------------------------------------------------------------------------------
        """)

        menyVal = input("-> ")
        if menyVal != bye:
            if menyVal == "1":
                plockaUpp()
            elif menyVal == "2":
                gåAv()
            elif menyVal == "3":
                skrivUt()
            elif menyVal == "4":
                sammanlagdÅlder()
            elif menyVal == "5":
                medelÅlder()
            elif menyVal == "6":
                äldst()
            elif menyVal == "7":
                busSort()
            elif menyVal == "8":
                hittaPassagerare()
            elif menyVal == "9":
                pass
            elif menyVal == "10":
                pass
        else:
            print('Nej')
print(
"""
                                           _____________
                                         _/_|[][][][][] | - -
                                        (      Bussen   | - -
                                        =--OO-------OO--=
""")

main()
