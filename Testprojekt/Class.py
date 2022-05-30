import operator as op
class Car(object):
    # Metoden __init__, körs alltid då ett objekt skapas
    def __init__(self, model, color, mileage):
        # Nedanstående variabler kallas för attribut
        self.model = model
        self.color = color
        self.mileage = mileage

    # Metoden getModel, skriver ut bilmodellen
    def getModel(self):
        # self.model refererar till atributet model, som finns i __init__()
        print(self.model)
        return
    def setModel(self, newModel):
        # Det nedan så ändras attributet model till det som metoden anropades med
        self.model = newModel

    def setColor(self, color):
        self.color = color

    def setMileage(self, newMileage):
        self.mileage = newMileage

    def getMileage(self):
        print(self.mileage)
        return

# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
aCar = Car('Volvo', 'Blå', 1587)
aCar.getModel()
aCar.setModel('Renault')
aCar.getModel()
bCar = Car('Toyota', 'röd', 1672)
bCar.getModel()
print(aCar.color)
theMileage = aCar.getMileage()
cCar = Car('Toyota', 'gul', 1999)
cCar.getModel()
dCar = Car('Ferrari', 'orange', 4000)
dCar.getModel()
print('-----------')
myCars = []
myCars.append(aCar.model)
myCars.append(bCar.model)
myCars.append(aCar.mileage)
myCars.append(dCar.model)
for model in myCars:
    print(f'{model}')


#print(sorted(myCars, key = op.attrgetter('model')))
