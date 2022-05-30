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

aPerson = Person('','','')

namnLista=['Love', 'Ashley', 'Charlie', 'Kim', 'Billie', 'Noa', 'Nico','Mika','Lee',
'Michele','Valentin','Minou','Lo','Cleo','Boobie', 'Robin', 'Jordan', 'Ziggy','Elliot','Eli','Dani','Taylor','Mango','Pixi','Filur']
könLista = ['Han', 'Hon' , 'Hen']
buss = []
def buss_sortÅlder(aPerson):
    return aPerson.ålder
def buss_sortNamn(aPerson):
    return aPerson.namn



# ------------------------- Funktionsdefinitioner ---------------------------- #


# Lägger till en ny person i bussen.
def plockaUpp():
    if sum(passagerare) >= 25:
        print('Fullt på bussen')
    else:

        namn = r.choice(namnLista)
        ålder = r.randint(0,100)
        kön = r.choice(könLista)
        buss.append(Person(namn,ålder,kön))



        passagerare.append(+1)
        print(f'Du plocka upp {namn}, {kön} är {ålder} år gammal, du har nu {sum(passagerare)} passagerare')
        return

    return




# Släpper av en person från bussen.
def gåAv():
    if len(buss) == 0:
        print('Du har inga passagerare så du kan inte släppa av någon')

    else:
        passagerare.append(-1)
        print(f'Du släppte av {buss[0:1]}, Du har nu {sum(passagerare)} passagerare')
        buss.pop(0)

        return

# Skriver ut alla passagerare på bussen.
def skrivUt():
        if len(buss) == 0:
            print('Ingen på bussen')
        else:
            for namn in buss:
                print(f'Din buss kör {namn}')
            return

# Skriver ut den sammanlagda åldern på alla passagerarna på bussen.
def sammanlagdÅlder():
    if len(buss) == 0:
        print('Ingen på bussen att beräkna medelåldern på')
    else:
        try:
            #print('Summan av alla åldrar på bussen är',sum(gamal))
            print('Summan av alla åldrar på bussen är -->',sum(Person.ålder for Person in buss))
        except:
            print('Finns ingen på bussen att beräkna medelåldern på')
    return

# Skriver ut medelåldern på alla passagerarna i bussen.
def medelÅlder():
    try:
        #print('Medelåldern på bussen är',sum(gamal)/len(gamal))
        print('Medelålder på alla passagerare på bussen är -->',sum(Person.ålder for Person in buss)/(len(buss)))
    except:
        print('Finns ingen på bussen att beräkna medelåldern på')
    return


# Skriver ut personen som är äldst på bussen.
def äldst():
    if len(buss) == 0:
        print('Det finns ingen som är äldst på bussen')
    else:
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
                        print(sorted(buss, key = buss_sortÅlder, reverse = True))
                    elif d == 2:
                        print(sorted(buss, key = buss_sortÅlder))

        except:
            print('Fel, försök igen!')
            return




# Skriver ut en lista på alla passagerare inom ett visst åldersspann som du själv väljer.
def hittaPassagerare():
    if len(buss) == 0:
        print('Ingen på bussen så du kan inte leta efter folk mellan åldrar')
    else:
        try:
            s = int(input("Vad är äldsta för ålderspannet?"))
            n = int(input("Vad är yngsta för ålderspannet?"))
            for n in range(n, s+1):
                for aPerson in buss:
                    if aPerson.ålder == n:
                        print(f'Passageraren {aPerson.namn} är {aPerson.ålder} år gammal och identifierar sig som {aPerson.kön}')

        except:
            print("Det du valde var inte ett giltigt alternativ, vänligen försök igen")

        return

# Skriver ut antal passagerare som har de olika könen.
def könAntal():
    if len(buss) == 0:
        print('Bussen är tom och därmet kan du icke skriva ut hur många som finns av alla kön!')
    else:
        print('Det sitter', sum(Person.kön == 'Han' for Person in buss),'st killar på din buss')
        print('Det sitter', sum(Person.kön == 'Hon' for Person in buss),'st tjejer på din buss')
        print('Det sitter', sum(Person.kön == 'Hen' for Person in buss),'st ickebinära personer på din buss')
# petar på en passagerare. Skriver ut en text som beskriver passagerarens
# reaktion när denne blir petad på. För lite svårare uppgift kan reaktionerna
# variera från person till person, t.ex. beroende på ålder.
def peta():
    reaktionBarn = ['Hejsan!', 'Vad gör du?', '*Slog dig på armen*', 'Sluta!',
    'Jag tänker säga till mamma!','AJ!', 'Jag ringer polisen','*Petade tillbaka*','*Säger till busschafören att kasta av dig*']
    reaktionUngdom = ['Vad vill du?','*Gav dig en konstig blick*',
    'Huh?', 'Tjena!', 'Ok?' , 'Vill du slåss?' , 'Ska vi slåss?','Ska jag kasta av dig eller?']
    reaktionVuxen = ['Kan jag hjälpa dig?' ,'*Tittar på dig*', 'Bussen går om 2 minuter', 'Ursäkta jag har brottom',
    'Ledsen jag läser tidningen']
    if len(buss) == 0:
        print('TOOOOMT PÅ BUSSEN!')
    else:
        s = r.choice(buss)

        if s.ålder <= 12:
            print('Du petade på', s,'och hans reaktion var -->',r.choice(reaktionBarn))
        elif s.ålder > 12 and s.ålder <=20:
            print('Du petade på', s,'och hans reaktion var -->',r.choice(reaktionUngdom))
        else:
            print('Du petade på', s,'och hans reaktion var -->',r.choice(reaktionVuxen))
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
            9. Skriv ut antal utav alla kön                     10. Peta på passagerare
            q. Avsluta
        ---------------------------------------------------------------------------------------
        """)

        menyVal = input("Vilket alternativ vill du göra? --> ")
        if menyVal != '1' and menyVal != '2' and menyVal != '3' and menyVal != '4' and menyVal != '5' and menyVal != '6' and menyVal != '7' and menyVal != '8' and menyVal != '9' and menyVal != '10' and menyVal != 'q':
            print('Tyvärr är', menyVal,'inte ett alternativ' )

        else:
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
                könAntal()
            elif menyVal == '10':
                peta()
            elif menyVal == 'q':
                if len(buss) == 0:
                    print('Programmet avslutas och du hade inga passagerare kvar på bussen')
                elif len(buss) == 1:
                    print('Programmet avslutades och du lämnade',buss ,'kvar på bussen vilket jag tror att de inte uppskattade')


print(
"""
                                           _____________
                                         _/_|[][][][][] | - -
                                        (      Bussen   | - -
                                        =--OO-------OO--=
""")

main()
