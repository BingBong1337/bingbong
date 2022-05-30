from tkinter import *
from tkinter import messagebox
root = Tk()



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


# Lägger till en ny person i bussen. Kan inte överstiga 25st samtidigt.
def plockaUpp():
    if sum(passagerare) >= 25:
        print('Fullt på bussen')
        print('------------------------------------------------------')
    else:

        namn = r.choice(namnLista)
        ålder = r.randint(0,100)
        kön = r.choice(könLista)
        buss.append(Person(namn,ålder,kön))



        passagerare.append(+1)
        print(f'Du plocka upp {namn}, {kön} är {ålder} år gammal, du har nu {sum(passagerare)} passagerare')
        print('------------------------------------------------------')
        return

    return




# Släpper av en person från bussen.
def gåAv():
    if len(buss) == 0:
        print('Du har inga passagerare så du kan inte släppa av någon')
        print('------------------------------------------------------')
    else:
        passagerare.append(-1)
        f = r.choice(buss)
        print('Du släppte av',f,f'Du har nu {sum(passagerare)} st passagerare' )
        buss.remove(f)
        #print(f'Du släppte av {buss[0:1]}, Du har nu {sum(passagerare)} passagerare')
        #buss.pop(0)
        print('------------------------------------------------------')
        return

# Skriver ut alla passagerare på bussen.
def skrivUt():
        if len(buss) == 0:
            print('Ingen på bussen')
            print('------------------------------------------------------')
        else:
            for passagerare in buss:
                print(f'Din buss kör {passagerare}')
            print('------------------------------------------------------')
            return

# Skriver ut den sammanlagda åldern på alla passagerarna på bussen.
def sammanlagdÅlder():
    if len(buss) == 0:
        print('Ingen på bussen att beräkna medelåldern på')
        print('------------------------------------------------------')
    else:
        try:
            #print('Summan av alla åldrar på bussen är',sum(gamal))
            print('Summan av alla åldrar på bussen är -->',sum(Person.ålder for Person in buss))
            print('------------------------------------------------------')
        except:
            print('Finns ingen på bussen att beräkna medelåldern på')
            print('------------------------------------------------------')
    return

# Skriver ut medelåldern på alla passagerarna i bussen.
def medelÅlder():
    try:
        #print('Medelåldern på bussen är',sum(gamal)/len(gamal))
        print('Medelålder på alla passagerare på bussen är -->',sum(Person.ålder for Person in buss)/(len(buss)))
        print('------------------------------------------------------')
    except:
        print('Finns ingen på bussen att beräkna medelåldern på')
        print('------------------------------------------------------')
    return


# Skriver ut personen som är äldst på bussen.
def äldst():
    if len(buss) == 0:
        print('Det finns ingen som är äldst på bussen')
        print('------------------------------------------------------')
    else:
        g = sorted(buss, key = buss_sortÅlder , reverse=True)
        print('Den äldsta passageraren på bussen är',g[0].namn,'som är',g[0].ålder,'och identifierar sig som en',g[0].kön)
        print('------------------------------------------------------')
        #print('Äldst:\n', sorted(buss, key = buss_sortÅlder, reverse=True))
        #print('------------------------------------------------------')

    return

# Sorterar bussen, antingen efter namn i bokstavsordning eller efter ålder.
def busSort():
    if len(buss) == 0:
        print('Det finns ingen att sortera på bussen')
        print('------------------------------------------------------')
    else:
        try:
            n = input('Vill du sortera bussen efter namn(n) eller ålder(å)?-->')
            print('------------------------------------------------------')
            if n != 'n' and n != 'å':
                print('Förlåt, jag förstod inte försök igen')
                print('------------------------------------------------------')
            else:
                if n == 'n':
                    s = int(input('Bokstavsårdning A-Ö(1) eller Ö-A(2) -->'))
                    print('------------------------------------------------------')
                    if s != 1 and s != 2:
                        print('Kan du ta om det?')
                        print('------------------------------------------------------')
                    if s == 1:
                        print(sorted(buss, key = buss_sortNamn))
                        print('------------------------------------------------------')
                    elif s == 2:
                        print(sorted(buss, key = buss_sortNamn, reverse = True))
                        print('------------------------------------------------------')
                elif n == 'å':
                    d = int(input('Äldst eller yngst?(1 för äldst... 2 för yngst)'))
                    if d != 1 and d != 2:
                        print('Kan du ta om det?')
                        print('------------------------------------------------------')
                    if d == 1:
                        print(sorted(buss, key = buss_sortÅlder, reverse = True))
                        print('------------------------------------------------------')
                    elif d == 2:
                        print(sorted(buss, key = buss_sortÅlder))
                        print('------------------------------------------------------')
        except:
            print('Fel, försök igen!')
            print('------------------------------------------------------')
            return




# Skriver ut en lista på alla passagerare inom ett visst åldersspann som du själv väljer.
def hittaPassagerare():
    if len(buss) == 0:
        print('Ingen på bussen så du kan inte leta efter folk mellan åldrar')
        print('------------------------------------------------------')
    else:
        try:
            s = int(input("Vad är äldst för ålderspannet-->?"))
            n = int(input("Vad är yngst för ålderspannet-->?"))
            for n in range(n, s+1):
                for aPerson in buss:
                    if aPerson.ålder == n:
                        print(f'Passageraren {aPerson.namn} är {aPerson.ålder} år gammal och identifierar sig som {aPerson.kön}')
            print('------------------------------------------------------')
        except:
            print("Det du valde var inte ett giltigt alternativ, vänligen försök igen")
            print('------------------------------------------------------')
        return

# Skriver ut antal passagerare av de olika könen.
def könAntal():
    if len(buss) == 0:
        print('Bussen är tom och därmet kan du icke skriva ut hur många som finns av alla kön!')
        print('------------------------------------------------------')
    else:
        print('Det sitter', sum(Person.kön == 'Han' for Person in buss),'st killar på din buss')
        print('Det sitter', sum(Person.kön == 'Hon' for Person in buss),'st tjejer på din buss')
        print('Det sitter', sum(Person.kön == 'Hen' for Person in buss),'st ickebinära personer på din buss')
        print('------------------------------------------------------')
#Petar på en passagerare för att se vilken reaktion den får, beror på ålder av passageraren.
def peta():
    reaktionBarn = ['Hejsan!', 'Vad gör du?', '*Slog dig på armen*', 'Sluta!',
    'Jag tänker säga till mamma!','AJ!', 'Jag ringer polisen','*Petade tillbaka*','*Säger till busschafören att kasta av dig*']
    reaktionUngdom = ['Vad vill du?','*Gav dig en konstig blick*',
    'Huh?', 'Tjena!', 'Ok?' , 'Vill du slåss?' , 'Ska vi slåss?','Ska jag kasta av dig eller?']
    reaktionVuxen = ['Kan jag hjälpa dig?' ,'*Tittar på dig*', 'Bussen går om 2 minuter', 'Ursäkta jag har brottom',
    'Ledsen jag läser tidningen']
    reaktionGammling = ['Känner jag dig?', 'God dag!', 'Kommer du ihåg 2010?, det var ett bra år',
     'Nej tack, jag vill inte ha några kakor','Ska du med och handla?','Får man bjuda på en kopp kaffe?',
     'Shit skatteverket har kommit för att ta mig!','Dig minns jag ej ha träffat!']
    if len(buss) == 0:
        print('Finns tyvärr ingen att peta på, du får plocka upp passagerare först')
        print('------------------------------------------------------')
    else:
        s = r.choice(buss)

        if s.ålder <= 12:
            print('Du petade på', s,'och', s.kön ,'reagerade på detta sätt-->',r.choice(reaktionBarn))
            print('------------------------------------------------------')
        elif s.ålder > 12 and s.ålder <=20:
            print('Du petade på', s,'och', s.kön ,'reagerade på detta sätt -->',r.choice(reaktionUngdom))
            print('------------------------------------------------------')
        elif s.ålder > 21 and s.ålder <=50:
            print('Du petade på', s,'och', s.kön ,'reagerade på detta sätt -->',r.choice(reaktionVuxen))
            print('------------------------------------------------------')
        else:
            print('Du petade på', s,'och', s.kön ,'reagerade på detta sätt -->', r.choice(reaktionGammling))
            print('------------------------------------------------------')
    return



# ------------------------------ Huvudprogram --------------------------------- #
Label = Label(root, text=    """
                                   _____________
                                 _/_|[][][][][] | - -
                                (      Bussen   | - -
                                =--OO-------OO--=
                                     --- MENY ---
                Välkommen till buss-simulatorn. Välj ett av alternativen nedan:

        1. Plocka upp ny passagerare                        2. Låt passagerare gå av
        3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
        5. Beräkna medelåldern                              6. Hitta äldst person
        7. Sortera bussen                                   8. Hitta personer inom ett specifikt åldersspann
        9. Skriv ut antal utav alla kön                     10. Peta på passagerare

    ---------------------------------------------------------------------------------------
    """)
root.title('Bussen')
#Funkar endast på min (Rufus) dator håll den grå.
#root.iconbitmap('c:/buss.ico')
Label.grid(row=0,column=5)
b1 = Button(root, text='(1)Plocka upp en passagerare',command=plockaUpp)
b2 = Button(root, text='(2)Släpp av en passagerere',command=gåAv)
b3 = Button(root, text='(3)Skriv ut alla som sitter på bussen',command=skrivUt)
b4 = Button(root, text='(4)Beräkna sammanlagd ålder av alla på bussen',command=sammanlagdÅlder)
b5 = Button(root, text='(5)Beräkna medelåldern på alla passagerare',command=medelÅlder)
b6 = Button(root, text='(6)Hitta äldsta personen som sitter på bussen',command=äldst)
b7 = Button(root, text='(7)Sortera bussen',command=busSort)
b8 = Button(root, text='(8)Hitta personer inom ett specifikt åldersspann',command=hittaPassagerare)
b9 = Button(root, text='(9)Skriv ut antal utav alla kön',command=könAntal)
b10 = Button(root, text='(10)Peta på en passagerare',command=peta)
b11 = Button(root, text='Avsluta Programmet',command=root.quit)
b1.grid(row=5,column=4)
b2.grid(row=5,column=6)
b3.grid(row=6,column=4)
b4.grid(row=6,column=6)
b5.grid(row=7,column=4)
b6.grid(row=7,column=6)
b7.grid(row=8,column=4)
b8.grid(row=8,column=6)
b9.grid(row=9,column=4)
b10.grid(row=9,column=6)
b11.grid(row=10,column=5)
root.mainloop()
#def main():
#    menyVal = ""


#    while menyVal != "q":
#        print(
#        """
#                                         --- MENY ---
#                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
#            1. Plocka upp ny passagerare                        2. Låt passagerare gå av
#            3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
#            5. Beräkna medelåldern                              6. Hitta äldst person
#            7. Sortera bussen                                   8. Hitta personer inom ett specifikt åldersspann
#            9. Skriv ut antal utav alla kön                     10. Peta på passagerare
#            q. Avsluta
#        ---------------------------------------------------------------------------------------
#        """)

#        menyVal = input("Vilket alternativ vill du göra? --> ")
#        if menyVal != '1' and menyVal != '2' and menyVal != '3' and menyVal != '4' and menyVal != '5' and menyVal != '6' and menyVal != '7' and menyVal != '8' and menyVal != '9' and menyVal != '10' and menyVal != 'q':
#            print('Tyvärr är', menyVal,'inte ett alternativ' )

#        else:
#            if menyVal == "1":
#                plockaUpp()
#            elif menyVal == "2":
#                gåAv()
#            elif menyVal == "3":
#                skrivUt()
#            elif menyVal == "4":
#                sammanlagdÅlder()
#            elif menyVal == "5":
#                medelÅlder()
#            elif menyVal == "6":
#                äldst()
#            elif menyVal == "7":
#                busSort()
#            elif menyVal == "8":
#                hittaPassagerare()
#            elif menyVal == "9":
#                könAntal()
#            elif menyVal == '10':
#                peta()
#            elif menyVal == 'q':
#                if len(buss) == 0:
#                    print('Programmet avslutas och du hade inga passagerare kvar på bussen')
#                elif len(buss) == 1:
#                    print('Programmet avslutades och du lämnade',buss ,'kvar på bussen vilket jag tror att de inte uppskattade')


#print(
#"""
#                                           _____________
#                                         _/_|[][][][][] | - -
#                                        (      Bussen   | - -
#                                        =--OO-------OO--=
#""")

#main()
