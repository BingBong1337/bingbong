import random as r

class Person():
    def __init__(self, namn, ålder, kön):
        self.namn = namn
        self.ålder = ålder
        self.kön = kön


    def __repr__(self):
        return '({},{},{})'. format(self.namn, self.ålder, self.kön)

namnLista=['Love', 'Ashley', 'Charlie', 'Kim', 'Billie', 'Noa', 'Nico','Mika','Lee',
'Michele','Valentin','Minou','Lo','Cleo','Boobie', 'Robin', 'Jordan', 'Ziggy','Elliot','Eli','Dani','Taylor','Mango','Pixi','Filur']
könLista = ['Han', 'Hon' , 'Hen']
buss = []

for i in range(10):
    namn = r.choice(namnLista)
    ålder = r.randint(0,100)
    kön = r.choice(könLista)
    buss.append(Person(namn,ålder,kön))
print(buss)

print('Det sitter', sum(Person.kön == 'Han' for Person in buss),'st killar på din buss')
print('Det sitter', sum(Person.kön == 'Hon' for Person in buss),'st tjejer på din buss')
print('Det sitter', sum(Person.kön == 'Hen' for Person in buss),'st ickebinära personer på din buss')