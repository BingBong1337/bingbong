import random as r


class Person(object):
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

def __repr__(self):
    return ('{},{}' .format(self.namn , self.ålder))

def setNamn(self, nyttNamn):
    self.namn = nyttNamn

def setÅlder(self, nyttÅlder):
    self.ålder = nyttÅlder

def getNamn(self):
    return self.namn

def getÅlder(self):
    return self.ålder
buss = []
namnLista = ['Love', 'Ashley', 'Charlie', 'Kim', 'Billie', 'Noa', 'Nico','Mika','Lee',
'Michele','Valentin','Minou','Lo','Cleo','Boobie', 'Robin', 'Jordan', 'Ziggy','Elliot','Eli','Dani','Taylor','Mango','Pixi','Filur']
Person = Person('','')
def namn():
    Person.namn = random.choice(namnLista)
    return
def ålder():
    Person.ålder = r.randint(0,100)
    return


def GåPå():
    namn()
    ålder()
    buss.append(Person)
    print(buss)
    pass
