import random as r
import operator as op

class MyNumber(object):
    def __init__(self, myNumber, myName):
        self.theNumber = myNumber
        self.theName = myName

    def __repr__(self):
        return('{},{}').format(self.theName,self.theNumber)
    def printNumber(self):
        print(self.theNumber)
        print(self.theName)

aNumber = (10)
bNumber = (20)

namnLista = ['Love', 'Ashley', 'Charlie', 'Kim', 'Billie', 'Noa', 'Nico','Mika','Lee',
'Michele','Valentin','Minou','Lo','Cleo','Boobie', 'Robin', 'Jordan', 'Ziggy','Elliot','Eli','Dani','Taylor','Mango','Pixi','Filur']
numberList = []
for i in range(1):
    theName = r.choice(namnLista)
    theNumber = r.randint(1,100)
    #numberList.append(theNumber)
    #numberList.append(theName)
    #numberList.append([theNumber, theName])
    numberList.append(MyNumber(theNumber,theName))
    print(numberList)
    
