import os
os.system('cls')
class Djur():
    def __init__(self, namn):
        self.namn = namn
    def ät(self):
        print('djuret äter')
    def sov(self):
        print('djuret sover')

class Fågel(Djur):
    def __init__(self,namn,vingspann):
        super().__init__(namn)
        self.vingspann = vingspann
class Fisk(Djur):
    def __init__(self,namn,maxdjup):
        super().__init__(namn)
        self.maxdjup = maxdjup
    def simma(self):
        print('fisken simmar')
class Torsk(Fisk):
    def __init__(self,namn,maxdjup,hastighet):
        super().__init__(namn,maxdjup)
        self.hastighet = hastighet

class Haj(Fisk):
    def __init__(self,namn,maxdjup,antalTänder):
        super().__init__(namn,maxdjup)
        self.antalTänder = antalTänder
    def ät(self,Djur):
        print(self.namn,'äter',Djur.namn)

torsk = Torsk('firre',1500,29)
haj = Haj('pen',1500, 6200)
def fånga(haj,torsk):
    if torsk.hastighet < 30 and haj.maxdjup <= torsk.maxdjup:
        return True
    else:
        return False
    
if fånga(haj,torsk) == True:
    print('True')
else:
    print('False')

fisk = Fisk('fishman',820)
haj.ät(fisk)
fisk.simma()
fisk.sov()
