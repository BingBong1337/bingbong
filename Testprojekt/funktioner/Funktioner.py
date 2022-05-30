# De båda funktionerna läsTal1() och läsTal2()


# nedan skiljer sig åt enbart med sin ledtext
# till användaren. Om en och samma ledtext
# accepteras så räcker det med en enda funktion.

# Funktion som läser in första talet
# Argument: inget.
# Returvärde: Det inlästa talet
def läsTal1():
    # Definiera funktionen och
    # returnera det inlästa talet
    tal1 = int(input('Ge mig ett tal -->'))
    return tal1
# Funktion som läser in andra talet
# Argument: inget.
# Returvärde: Det inlästa talet
def läsTal2():
    # Implementera funktionen och
    # returnera det inlästa talet
    tal2 = int(input('Ge mig ytterliggare tal -->'))
    return tal2
# ---------------------------------------
# Funktion som adderar två tal
# Argument: de båda talen
# Returvärde: Summan
def adderare(tal1, tal2):
    # Implementera funktionen och
    # returnera summan
    summa = tal1 + tal2
    return summa
# Funktion som subtraherar två tal
# Argument: de båda talen
# Returvärde: differensen
def subtraherare(tal1, tal2):
    # Implementera funktionen och
    # returnera dífferensen
    differens = tal1 - tal2
    return differens
# Funktion som multiplicerar två tal
# Argument: de båda talen
# Returvärde: produkten
def multiplicerare(tal1, tal2):
    # Implementera funktionen och
    # returnera produkten
    produkt = tal1 * tal2
    return produkt
# ---------------------------------------
# Här sker körningen av huvudprogrammet
# Argument: inget
# Returvärde: inget
def main():
    operator = '' # Variabeln måste deklareras innan den används nedan

    while operator != 'q':
        # Då """dessa citationstecken""" används så kan strängen innehålla radbrytningar
        operator = input("""Ange räknesätt vill du använda (q avslutar)
        (a)ddition   (s)ubtraktion   (m)ultiplikation
        -> """)

        # Om addition väljs
        if operator == 'a':
            # Anropa lämpliga funktioner här
            tal1 = läsTal1()
            tal2 = läsTal2()
            summa = adderare(tal1, tal2)
            print(f'{summa}')
        # Om subtraktion väljs
        elif operator == 's':
            # Anropa lämpliga funktioner här
            tal1 = läsTal1()
            tal2 = läsTal2()
            differens = subtraherare(tal1, tal2)
            print(f'{differens}')
        # Om multiplikation väljs
        elif operator == 'm':
            # Anropa lämpliga funktioner här
            tal1 =läsTal1()
            tal2 = läsTal2()
            produkt = multiplicerare(tal1, tal2)
            print(f'{produkt}')
        # Om avluta väljs
        elif operator == 'q':
            break # Går ur loopen och återvänder till
                  # raden efter main() anropades.

        # Om något icke-definierat val görs
        # så fångas det upp av else-satsen
        else:
            print("Alternativet saknas, försök igen")
            # Här lämnas if-satsen och programmet går ut
            # till nivån närmast "ovanför" denna, dvs
            # loopen där val görs.


# Här börjar programmets körning
# ---------------------------------------
main()

# När det avslutas normalt kommer det hit
print("Programmet avslutades normalt")
